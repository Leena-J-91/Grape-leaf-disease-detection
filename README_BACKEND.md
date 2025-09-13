# Grape Leaf Disease Detection - Backend Deployment

This guide will help you deploy the Flask backend to Render's free tier.

## Prerequisites

1. A GitHub account
2. A Render account (sign up at [render.com](https://render.com))
3. Your code pushed to a GitHub repository

## Step-by-Step Deployment Instructions

### 1. Prepare Your Repository

Make sure your repository contains:
- `app.py` (your Flask application)
- `requirements.txt` (Python dependencies)
- `Dockerfile` (for containerized deployment)
- `grape_disease_classifier.h5` (your trained model)
- `static/` folder (if you have static files)
- `templates/` folder (if you have HTML templates)

### 2. Create a Render Web Service

1. **Log in to Render**
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" and select "Web Service"

2. **Connect Your Repository**
   - Choose "Build and deploy from a Git repository"
   - Connect your GitHub account if not already connected
   - Select your repository containing the grape disease detection project

3. **Configure the Service**
   - **Name**: `grape-disease-backend` (or any name you prefer)
   - **Environment**: `Docker`
   - **Region**: Choose the closest region to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (uses root directory)
   - **Dockerfile Path**: `Dockerfile` (should be auto-detected)

4. **Advanced Settings**
   - **Auto-Deploy**: `Yes` (deploys automatically on git push)
   - **Health Check Path**: `/` (your home route)

5. **Environment Variables** (if needed)
   - You can add environment variables in the Render dashboard if your app needs them
   - For this project, no additional environment variables are required

### 3. Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Build the Docker image
   - Deploy your application
3. Wait for the deployment to complete (usually 5-10 minutes)

### 4. Get Your Backend URL

1. Once deployed, you'll see a URL like: `https://grape-disease-backend.onrender.com`
2. **Important**: Save this URL - you'll need it for your frontend configuration
3. Test your API by visiting: `https://your-app-name.onrender.com/`

### 5. Configure CORS (if needed)

If you encounter CORS issues when connecting your frontend, you may need to add CORS support to your Flask app. Add this to your `app.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
```

And add `flask-cors==4.0.0` to your `requirements.txt`.

## Important Notes

### Free Tier Limitations
- **Sleep Mode**: Your app will sleep after 15 minutes of inactivity
- **Cold Start**: First request after sleep may take 30+ seconds
- **Build Time**: 500 build minutes per month
- **Bandwidth**: 100GB per month

### Model File Size
- Your `grape_disease_classifier.h5` file should be included in your repository
- If it's too large (>100MB), consider using Git LFS or hosting it separately

### Environment Variables
- You can set environment variables in the Render dashboard
- Useful for API keys, database URLs, etc.

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check that all dependencies are in `requirements.txt`
   - Ensure your Dockerfile is correct
   - Check the build logs in Render dashboard

2. **App Crashes on Startup**
   - Verify your model file exists and is accessible
   - Check that all required files are in the repository
   - Review the deployment logs

3. **CORS Errors**
   - Add `flask-cors` to requirements.txt
   - Enable CORS in your Flask app

4. **Slow Response Times**
   - This is normal for free tier due to sleep mode
   - Consider upgrading to paid plan for production use

### Getting Help
- Check Render's documentation: [render.com/docs](https://render.com/docs)
- Review your deployment logs in the Render dashboard
- Ensure your local app works before deploying

## Next Steps

After successful deployment:
1. Note your backend URL (e.g., `https://your-app.onrender.com`)
2. Use this URL in your frontend configuration
3. Test the API endpoints to ensure they work correctly

Your backend is now ready to serve your frontend application!
