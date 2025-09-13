import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from PIL import Image # type: ignore
import io

app = Flask(__name__)

model = load_model('grape_disease_classifier.h5', compile=False) 

categories = ['Black Measles Disease', 'Black Rot Disease', 'Healthy', 'Leaf Blight Disease']

def prepare_image(img):
    img = Image.open(img)
    img = img.resize((224, 224))  
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0) 
    
    return img_array

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'message': 'No image file provided'}), 400

    img_file = request.files['image']
    img_array = prepare_image(img_file)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    result = categories[predicted_class[0]]
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
