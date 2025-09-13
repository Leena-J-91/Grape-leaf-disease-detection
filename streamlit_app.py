import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import base64

# Page configuration
st.set_page_config(
    page_title="ದ್ರಾಕ್ಷಿ ಎಲೆ ರೋಗ ಸ್ಕ್ಯಾನರ್",
    page_icon="🍇",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to replicate your original design
st.markdown("""
<style>
    .main {
        background-image: url('data:image/jpeg;base64,{background_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    .container {
        max-width: 600px;
        margin: 50px auto;
        background-color: rgba(255, 255, 255, 0.9);
        color: #333;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    
    .title {
        color: #4CAF50;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    
    .description {
        font-size: 1.2rem;
        margin-bottom: 30px;
        color: #555;
    }
    
    .upload-section {
        margin: 20px 0;
    }
    
    .result-box {
        margin-top: 20px;
        padding: 15px;
        background-color: #f4f4f4;
        color: #333;
        border-radius: 5px;
        font-size: 18px;
        border: 2px solid #4CAF50;
    }
    
    .treatment-box {
        margin-top: 20px;
        text-align: left;
        font-size: 16px;
        line-height: 1.6;
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
    }
    
    .treatment-title {
        color: #329635;
        font-size: 1.5rem;
        margin-bottom: 15px;
    }
    
    .treatment-subtitle {
        color: #4CAF50;
        font-size: 1.2rem;
        margin: 15px 0 10px 0;
    }
    
    .treatment-list {
        margin: 10px 0;
        padding-left: 20px;
    }
    
    .treatment-list li {
        margin: 8px 0;
    }
    
    .youtube-link {
        color: #4CAF50;
        text-decoration: none;
        font-weight: bold;
    }
    
    .youtube-link:hover {
        color: #388E3C;
    }
    
    .healthy-message {
        color: #4CAF50;
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        background-color: #e8f5e8;
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Load background image
def get_background_image():
    try:
        with open("static/image3.jpeg", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

# Load the ML model
@st.cache_resource
def load_ml_model():
    try:
        # Try different model loading approaches
        model_path = 'grape_disease_classifier.h5'
        
        # Check if model file exists
        import os
        if not os.path.exists(model_path):
            st.error(f"Model file not found: {model_path}")
            return None
            
        # Load model with error handling
        model = load_model(model_path, compile=False)
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.error("Please ensure the model file is in the root directory")
        return None

# Prepare image for prediction
def prepare_image(img):
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Get treatment recommendations
def get_treatment_recommendations(prediction):
    treatments = {
        "Black Measles Disease": """
        <div class="treatment-box">
            <h1>ಬ್ಲಾಕ್ ಮೀಸಲ್ಸ್ ರೋಗ</h1>
            <h3>ಬ್ಲಾಕ್ ಮೀಸಲ್ಸ್ ರೋಗಕ್ಕೆ ಚಿಕಿತ್ಸೆ:</h3>
            <h4>ರಾಸಾಯನಿಕ ಗೊಬ್ಬರಗಳ ಚಿಕಿತ್ಸೆಗಳು:-</h4>
            <ul class="treatment-list">
                <li>ಪೊಟಾಷಿಯಮ್ ಸಲ್ಫೇಟ್: ಒಟ್ಟಾರೆ ದ್ರಾಕ್ಷಿ ಬೆಳ್ಳೆಹೊಕ್ಕಿನ ಆರೋಗ್ಯವನ್ನು ಸುಧಾರಿಸುತ್ತದೆ ಮತ್ತು ರೋಗ ಪ್ರತಿರೋಧಕ ಶಕ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.</li>
                <li>ಮ್ಯಾಗ್ನೀಷಿಯಮ್ ಸಲ್ಫೇಟ್: ಮ್ಯಾಗ್ನೀಷಿಯಮ್ ಕೊರತೆಯನ್ನು ಸರಿಪಡಿಸುತ್ತದೆ ಮತ್ತು ಎಲೆಗಳಲ್ಲಿ ಹಚ್ಚುಕೊಲೆ (ಕ್ಲೋರೋಸಿಸ್) ತಡೆಯುತ್ತದೆ.</li>
                <li>ಜಿಂಕ್ ಸಲ್ಫೇಟ್: ಬೆಳ್ಳೆಹೊಕ್ಕಿನ ಬೆಳವಣಿಗೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ ಮತ್ತು ಶಿಲೀಂಧ್ರದ ಸೋಂಕುಗಳಿಗೆ ಪ್ರತಿರೋಧಶಕ್ತಿಯನ್ನು ಬಲಪಡಿಸುತ್ತದೆ.</li>
            </ul>
            <h4>ಸಾವಯವ ಚಿಕಿತ್ಸೆ:-</h4>
            <ul class="treatment-list">
                <li>ಬೇವಿನ ಎಣ್ಣೆ ಸ್ಪ್ರೇ: ಎಲೆಗಳಲ್ಲಿ ಶಿಲೀಂಧ್ರದ ಬೆಳವಣಿಗೆಯನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ ಮತ್ತು ಸಸ್ಯದ ರೋಗ ನಿರೋಧಕ ಶಕ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.</li>
                <li>ಬೋರ್ಡೆಕ್ಸ್ ಮಿಶ್ರಣ: ಶಿಲೀಂಧ್ರದ ಸೋಂಕಿನಿಂದ ಎಲೆಗಳನ್ನು ರಕ್ಷಿಸಲು ತಾಮ್ರ ಆಧಾರಿತ ದ್ರಾವಣವನ್ನು ಅನ್ವಯಿಸಿ.</li>
                <li>ಕಾಂಪೋಸ್ಟ್ ಟೀ: ಸಸ್ಯದ ಆರೋಗ್ಯ ಮತ್ತು ಮೈಕ್ರೋಬಿಯಲ್ ಚಟುವಟಿಕೆಯನ್ನು ಉತ್ತೇಜಿಸಲು ಹೂವಿನ ಸ್ಪ್ರೇ ಆಗಿ ಬಳಸಿರಿ.</li>
                <li><a href="https://www.youtube.com/watch?v=leUDkwJuz1o&pp=ygUfZ3JhcGUgcGxhbnQgdHJlYXRtZW50IGluIGthbm5kYQ%3D%3D" target="_blank" class="youtube-link">youtube ಲಿಂಕ್ (fertilizer)</a></li>
            </ul>
        </div>
        """,
        
        "Black Rot Disease": """
        <div class="treatment-box">
            <h1>ಬ್ಲಾಕ್ ರೋಟ್ ರೋಗ</h1>
            <h3>ಬ್ಲಾಕ್ ರೋಟ್ ರೋಗಕ್ಕೆ ಚಿಕಿತ್ಸೆ:</h3>
            <h4>ರಾಸಾಯನಿಕ ಗೊಬ್ಬರಗಳ ಚಿಕಿತ್ಸೆಗಳು:-</h4>
            <ul class="treatment-list">
                <li>ಸಮತೋಲಿತ ಎರೆಹುಡಿ: ಸಸ್ಯದ ಆರೋಗ್ಯ ಮತ್ತು ರೋಗ ಪ್ರತಿರೋಧ ಶಕ್ತಿಯನ್ನು ಸುಧಾರಿಸಲು 10-10-10 NPK ಎರೆಹುಡಿ ಬಳಸಿ.</li>
                <li>ಕ್ಯಾಲ್ಸಿಯಮ್ ನೈಟ್ರೇಟ್ ಸ್ಪ್ರೇ: ಪ್ರತಿ ಎರಡು ವಾರಕ್ಕೊಮ್ಮೆ 2-3 ಗ್ರಾಂ ಕ್ಯಾಲ್ಸಿಯಮ್ ನೈಟ್ರೇಟ್ ಅನ್ನು ಪ್ರತಿ ಲೀಟರ್ ನೀರಿನಲ್ಲಿ घೋಳಿಸಿ, ಎಲೆಕೋಶಗಳನ್ನು ಬಲಪಡಿಸಿ.</li>
                <li>ಪೊಟಾಷಿಯಮ್ ಸಲ್ಫೇಟ್: ಪ್ರತಿಯೊಂದು ಏಕರಿಗೆ 20-25 ಕೆ.ಜಿ ಪೊಟಾಷಿಯಮ್ ಸಲ್ಫೇಟ್ ಅನ್ನು ಅನ್ವಯಿಸಿ, ಪ್ರತಿರೋಧಶಕ್ತಿಯನ್ನು ಮತ್ತು ಬೆಳವಣಿಗೆಯನ್ನು ಹೆಚ್ಚಿಸು.</li>
            </ul>
            <h4>ಸಾವಯವ ಚಿಕಿತ್ಸೆ:-</h4>
            <ul class="treatment-list">
                <li>ಬೇವಿನ ಎಣ್ಣೆ ಸ್ಪ್ರೇ: ಪ್ರತಿಯೊಂದು ಲೀಟರ್ ನೀರಿನಲ್ಲಿ 2-3 ಟೀಸ್ಪೂನ್ ನೀಮ್ ಎಣ್ಣೆ ಹಾಕಿ, ಶಿಲೀಂಧ್ರದ ಬೆಳವಣಿಗೆಯನ್ನು ತಡೆಯಿರಿ.</li>
                <li>ಅಡಿಗೆ ಸೋಡಾ: ಪ್ರತಿ ಎರಡು ವಾರಕ್ಕೆ 1 ಟೇಬಲ್ ಸ್ಪೂನ್ ಬೇಕಿಂಗ್ ಸೋಡಾ, 1 ಟೀಸ್ಪೂನ್ ಎಣ್ಣೆ ಮತ್ತು 1 ಲೀಟರ್ ನೀರಿನ ಮಿಶ್ರಣವನ್ನು ಸ್ಪ್ರೇ ಮಾಡಿ.</li>
                <li>ಬೆಳ್ಳುಳ್ಳಿ ಸಾರ ಸ್ಪ್ರೇ: ಹೋಳಿಯನ್ನು ಮಿಕ್ಸ್ ಮಾಡಿ ಮತ್ತು ನೀರಿನಲ್ಲಿ ಹದವಾಗಿ ಕರಿದು, ಪ್ರತಿ ವಾರಕ್ಕೆ ಪ್ರಕೃತಿಕ ಫಂಗಸ್ ವಿರೋಧಿ ಚಿಕಿತ್ಸೆ ಮಾಡಿ.</li>
                <li><a href="https://www.youtube.com/watch?v=leUDkwJuz1o&pp=ygUfZ3JhcGUgcGxhbnQgdHJlYXRtZW50IGluIGthbm5kYQ%3D%3D" target="_blank" class="youtube-link">youtube ಲಿಂಕ್ (fertilizer)</a></li>
            </ul>
        </div>
        """,
        
        "Leaf Blight Disease": """
        <div class="treatment-box">
            <h1>ಬ್ಲೈಟ್ ರೋಗ</h1>
            <h3>ಬ್ಲೈಟ್ ರೋಗಕ್ಕೆ ಚಿಕಿತ್ಸೆ:</h3>
            <h4>ರಾಸಾಯನಿಕ ಗೊಬ್ಬರಗಳ ಚಿಕಿತ್ಸೆಗಳು:-</h4>
            <ul class="treatment-list">
                <li>ಸಮತೋಲಿತ NPK ಎರೆಹುಡಿ: ಒಟ್ಟಾರೆ ಸಸ್ಯದ ಆರೋಗ್ಯವನ್ನು ಸುಧಾರಿಸುತ್ತದೆ, ರೋಗಗಳಿಗೆ ಪ್ರತಿರೋಧಶಕ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.</li>
                <li>ಪೊಟಾಷಿಯಮ್ ಸಲ್ಫೇಟ್: ಸಸ್ಯದ ಕೋಶಭಿತ್ತಿಗಳನ್ನು ಬಲಪಡಿಸುತ್ತದೆ, ಇದರಿಂದ ಶಿಲೀಂಧ್ರ ಸೋಂಕುಗಳಿಗೆ ಪ್ರತಿರೋಧವನ್ನೂ ಹೆಚ್ಚಿಸುತ್ತದೆ.</li>
                <li>ಮ್ಯಾಗ್ನೀಷಿಯಮ್ ಸಲ್ಫೇಟ್: ಮ್ಯಾಗ್ನೀಷಿಯಮ್ ಕೊರತೆಯನ್ನು ತಡೆಯುತ್ತದೆ, ಇದು ಸಸ್ಯಗಳನ್ನು ಒತ್ತಡ ಮತ್ತು ರೋಗಗಳಿಗೆ ಹೆಚ್ಚು ಪ್ರತಿಕೂಲವಾಗಿಸುವುದನ್ನು ತಡೆಯುತ್ತದೆ.</li>
            </ul>
            <h4>ಸಾವಯವ ಚಿಕಿತ್ಸೆ:-</h4>
            <ul class="treatment-list">
                <li>ಬೇವಿನ ಎಣ್ಣೆ: ಪ್ರಕೃತಿಕ ಫಂಗಿಸೈಡ್ ಆಗಿದ್ದು, ಎಲೆಗಳಲ್ಲಿ ಶಿಲೀಂಧ್ರ ಬೆಳವಣಿಗೆಯನ್ನು ನಿಯಂತ್ರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.</li>
                <li>ಬೋರ್ಡೋ ಮಿಶ್ರಣ: ತಾಮ್ರ ಆಧಾರಿತ ದ್ರಾವಣ, ಇದು ಎಲೆಗಳನ್ನು ಶಿಲೀಂಧ್ರ ಸೋಂಕುಗಳಿಂದ ರಕ್ಷಿಸುತ್ತದೆ.</li>
                <li>ಹಾರ್ಸ್ಟೇಲ್ ಸಾರ: ಪ್ರಕೃತಿಕ ಫಂಗಸ್ ವಿರೋಧಿಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಸಸ್ಯದ ರೋಗಕಾರಕಗಳ ವಿರುದ್ಧ ರಕ್ಷಣೆ ಬಲಪಡಿಸುತ್ತದೆ.</li>
                <li><a href="https://www.youtube.com/watch?v=leUDkwJuz1o&pp=ygUfZ3JhcGUgcGxhbnQgdHJlYXRtZW50IGluIGthbm5kYQ%3D%3D" target="_blank" class="youtube-link">youtube ಲಿಂಕ್ (fertilizer)</a></li>
            </ul>
        </div>
        """,
        
        "Healthy": """
        <div class="healthy-message">
            <h4>ನಿಮ್ಮ ಸಸ್ಯ ಆರೋಗ್ಯಕರವಾಗಿದೆ! ಯಾವುದೇ ಚಿಕಿತ್ಸೆ ಅಗತ್ಯವಿಲ್ಲ. ಉತ್ತಮ ಕೆಲಸ ಮುಂದುವರಿಸಿ!</h4>
        </div>
        """
    }
    return treatments.get(prediction, "")

# Main app
def main():
    # Load background image
    background_image = get_background_image()
    
    # Main container
    st.markdown(f"""
    <div class="container">
        <h1 class="title">ದ್ರಾಕ್ಷಿ ಎಲೆ ರೋಗ ಸ್ಕ್ಯಾನರ್</h1>
        <p class="description">ಅದರ ಆರೋಗ್ಯವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಮತ್ತು ಚಿಕಿತ್ಸೆಯ ಶಿಫಾರಸುಗಳನ್ನು ಪಡೆಯಲು ದ್ರಾಕ್ಷಿ ಎಲೆಯ ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load model
    model = load_ml_model()
    if model is None:
        st.error("Model could not be loaded. Please check if the model file exists.")
        return
    
    # File uploader
    uploaded_file = st.file_uploader(
        "ಚಿತ್ರವನ್ನು ಸ್ಕ್ಯಾನ್ ಮಾಡಿ",
        type=['jpg', 'jpeg', 'png'],
        help="Upload an image of a grape leaf for disease detection"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Process image and make prediction
        if st.button("ಚಿತ್ರವನ್ನು ಸ್ಕ್ಯಾನ್ ಮಾಡಿ", type="primary"):
            with st.spinner("Processing image..."):
                try:
                    # Prepare image
                    img_array = prepare_image(image)
                    
                    # Make prediction
                    predictions = model.predict(img_array)
                    predicted_class = np.argmax(predictions, axis=1)
                    confidence = float(np.max(predictions))
                    
                    # Get categories
                    categories = ['Black Measles Disease', 'Black Rot Disease', 'Healthy', 'Leaf Blight Disease']
                    result = categories[predicted_class[0]]
                    
                    # Display result
                    st.markdown(f"""
                    <div class="result-box">
                        <strong>ಊಹಿಸಿದ ರೋಗ: {result}</strong><br>
                        <small>Confidence: {confidence:.2%}</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display treatment recommendations
                    treatment_html = get_treatment_recommendations(result)
                    st.markdown(treatment_html, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
