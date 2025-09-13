# Vercel Deployment Guide for Grape Leaf Disease Detection

## ⚠️ Important Notes

**This project can be deployed on Vercel, but there are some limitations:**

1. **Model Size**: The `grape_disease_classifier.h5` file is ~128MB, which exceeds Vercel's serverless function size limit (50MB)
2. **Cold Start**: TensorFlow models may cause slow cold starts in serverless functions
3. **Memory Limits**: Vercel has memory constraints that may affect model loading

## 🚀 Deployment Steps

### Option 1: Deploy with Model Optimization (Recommended)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy the project**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Set up and deploy? `Y`
   - Which scope? (Choose your account)
   - Link to existing project? `N`
   - Project name: `grape-disease-detection`
   - Directory: `.` (current directory)

### Option 2: Deploy via Vercel Dashboard

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration

## 🔧 Configuration Files

The project has been configured with:

- `vercel.json`: Routes API calls to serverless functions
- `api/predict.py`: Main prediction endpoint
- `api/requirements.txt`: Python dependencies for the API
- `.vercelignore`: Excludes large files from deployment

## ⚡ Model Size Solutions

### Option A: Use a Smaller Model
Consider training a lighter model or using model quantization:

```python
# Example quantization (add to your training script)
import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model('grape_disease_classifier.h5')

# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save the smaller model
with open('grape_disease_classifier.tflite', 'wb') as f:
    f.write(tflite_model)
```

### Option B: Use External Model Storage
Store the model on a CDN or cloud storage and load it dynamically:

```python
# In api/predict.py, replace model loading with:
import requests

def load_model_from_url():
    model_url = "https://your-cdn.com/grape_disease_classifier.h5"
    response = requests.get(model_url)
    # Load model from response content
```

### Option C: Use Vercel Pro Plan
Vercel Pro allows larger serverless functions (up to 1GB), but this requires a paid subscription.

## 🧪 Testing the Deployment

1. **Test the API endpoint**:
   ```bash
   curl -X POST https://your-app.vercel.app/api/predict \
     -F "image=@test_image.jpg"
   ```

2. **Test the frontend**:
   - Visit your Vercel URL
   - Upload a test image
   - Check if prediction works

## 🐛 Troubleshooting

### Common Issues:

1. **Function timeout**: Increase `maxDuration` in `vercel.json`
2. **Memory errors**: The model might be too large
3. **Cold start delays**: First request may take 10-30 seconds

### Debug Commands:

```bash
# Check deployment logs
vercel logs

# Check function status
vercel functions list

# Redeploy if needed
vercel --prod
```

## 📁 Project Structure After Deployment

```
your-vercel-app/
├── api/
│   ├── predict.py          # Serverless function
│   └── requirements.txt    # Python dependencies
├── templates/
│   └── index.html         # Frontend
├── static/
│   ├── config.js          # API configuration
│   └── image3.jpeg        # Background image
├── vercel.json            # Vercel configuration
└── grape_disease_classifier.h5  # Model file (if small enough)
```

## 🎯 Next Steps

1. **Deploy and test** with the current setup
2. **Monitor performance** and cold start times
3. **Consider model optimization** if performance is poor
4. **Set up monitoring** with Vercel Analytics

## 📞 Support

If you encounter issues:
1. Check Vercel deployment logs
2. Test the API endpoint directly
3. Consider the model size limitations
4. Review Vercel's serverless function documentation
