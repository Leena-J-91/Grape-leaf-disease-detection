import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Global variable to store the model (loaded once)
model = None

def load_model_once():
    """Load the model only once when the function is first called"""
    global model
    if model is None:
        try:
            # Load the model from the root directory
            model = load_model('grape_disease_classifier.h5', compile=False)
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
            model = None
    return model

def prepare_image(img_data):
    """Prepare image for prediction"""
    try:
        # If img_data is base64 encoded
        if isinstance(img_data, str):
            img_data = base64.b64decode(img_data)
        
        # Open image from bytes
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    except Exception as e:
        print(f"Error preparing image: {e}")
        return None

@app.route('/api/predict', methods=['POST'])
def predict():
    """Main prediction endpoint"""
    try:
        # Load model if not already loaded
        model = load_model_once()
        if model is None:
            return jsonify({'error': 'Model not available'}), 500
        
        # Check if image is provided
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        img_file = request.files['image']
        if img_file.filename == '':
            return jsonify({'error': 'No image file selected'}), 400
        
        # Read image data
        img_data = img_file.read()
        
        # Prepare image for prediction
        img_array = prepare_image(img_data)
        if img_array is None:
            return jsonify({'error': 'Invalid image format'}), 400
        
        # Make prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        
        # Define categories
        categories = ['Black Measles Disease', 'Black Rot Disease', 'Healthy', 'Leaf Blight Disease']
        
        # Get prediction result
        result = categories[predicted_class[0]]
        confidence = float(np.max(predictions))
        
        return jsonify({
            'prediction': result,
            'confidence': confidence,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in prediction: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'})

# This is required for Vercel
def handler(request):
    return app(request.environ, lambda *args: None)

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
