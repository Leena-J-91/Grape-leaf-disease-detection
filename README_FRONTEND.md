# Grape Leaf Disease Detection - Frontend Deployment

This guide will help you deploy your HTML/JavaScript frontend to Vercel's free tier and connect it to your Render backend.

## Prerequisites

1. A GitHub account
2. A Vercel account (sign up at [vercel.com](https://vercel.com))
3. Your backend already deployed on Render (get the URL from your backend deployment)

## Step-by-Step Deployment Instructions

### 1. Prepare Your Frontend

Your frontend should include:
- `templates/index.html` (your main HTML file)
- `static/config.js` (configuration file for backend URL)
- `static/image3.jpeg` (background image)
- `vercel.json` (Vercel configuration)

### 2. Configure Backend URL

**Important**: Before deploying, you need to update the backend URL in your configuration.

1. **Open `static/config.js`**
2. **Replace the placeholder URL**:
   ```javascript
   const config = {
     // Replace this with your actual Render backend URL
     API_URL: 'https://your-actual-backend-app.onrender.com',
     // ... rest of config
   };
   ```

3. **Example**:
   If your Render backend URL is `https://grape-disease-backend.onrender.com`, update it to:
   ```javascript
   API_URL: 'https://grape-disease-backend.onrender.com',
   ```

### 3. Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Log in to Vercel**
   - Go to [vercel.com](https://vercel.com) and sign in
   - Click "New Project"

2. **Import Your Repository**
   - Connect your GitHub account if not already connected
   - Select your repository containing the grape disease detection project
   - Click "Import"

3. **Configure the Project**
   - **Project Name**: `grape-disease-frontend` (or any name you prefer)
   - **Framework Preset**: `Other` (since this is a static HTML/JS project)
   - **Root Directory**: Leave as `.` (root directory)
   - **Build Command**: Leave empty (not needed for static files)
   - **Output Directory**: Leave empty (Vercel will auto-detect)

4. **Environment Variables** (Optional)
   - You can set `REACT_APP_API_URL` here if you prefer environment variables
   - But the `config.js` approach is simpler for this setup

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (usually 1-2 minutes)

#### Option B: Deploy via Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Link to existing project or create new one
   - Confirm settings
   - Wait for deployment

### 4. Get Your Frontend URL

1. Once deployed, you'll get a URL like: `https://grape-disease-frontend.vercel.app`
2. Your app is now live and accessible to users!

### 5. Test Your Deployment

1. **Visit your Vercel URL**
2. **Upload a grape leaf image**
3. **Verify the prediction works**
4. **Check browser console** for any errors

## Configuration Options

### Method 1: Using config.js (Current Setup)

**Pros**: Simple, no build process needed
**Cons**: URL is hardcoded in the file

To update the backend URL:
1. Edit `static/config.js`
2. Change the `API_URL` value
3. Commit and push to GitHub
4. Vercel will auto-deploy the changes

### Method 2: Using Environment Variables

If you prefer environment variables:

1. **In Vercel Dashboard**:
   - Go to your project settings
   - Add environment variable: `REACT_APP_API_URL`
   - Set value to your Render backend URL

2. **Update your HTML** to use environment variables:
   ```javascript
   const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
   ```

## Important Notes

### Free Tier Limitations
- **Bandwidth**: 100GB per month
- **Build Time**: 6000 build minutes per month
- **Custom Domains**: 1 custom domain per project
- **No sleep mode** (unlike Render free tier)

### CORS Configuration

If you encounter CORS errors, you may need to add CORS support to your Flask backend:

1. **Add to your Flask app** (`app.py`):
   ```python
   from flask_cors import CORS
   
   app = Flask(__name__)
   CORS(app)  # Enable CORS for all routes
   ```

2. **Add to requirements.txt**:
   ```
   flask-cors==4.0.0
   ```

3. **Redeploy your backend** to Render

### File Structure for Vercel

Your project structure should look like:
```
your-project/
├── templates/
│   └── index.html
├── static/
│   ├── config.js
│   └── image3.jpeg
├── vercel.json
└── README_FRONTEND.md
```

## Troubleshooting

### Common Issues

1. **CORS Errors**
   - Add CORS support to your Flask backend
   - Ensure your backend URL is correct in `config.js`

2. **404 Errors**
   - Check that your `vercel.json` is configured correctly
   - Ensure all file paths are correct

3. **Images Not Loading**
   - Verify image paths in your HTML
   - Check that images are in the `static/` folder

4. **API Calls Failing**
   - Verify your backend URL in `config.js`
   - Check that your backend is deployed and running
   - Test your backend URL directly in browser

### Getting Help

- Check Vercel's documentation: [vercel.com/docs](https://vercel.com/docs)
- Review your deployment logs in Vercel dashboard
- Test your backend API endpoints separately

## Updating Your Deployment

### To Update Backend URL:
1. Edit `static/config.js`
2. Change the `API_URL` value
3. Commit and push to GitHub
4. Vercel will automatically redeploy

### To Update Frontend Code:
1. Make your changes
2. Commit and push to GitHub
3. Vercel will automatically redeploy

## Next Steps

After successful deployment:
1. Test your complete application flow
2. Share your Vercel URL with users
3. Monitor usage and performance
4. Consider upgrading to paid plans for production use

Your frontend is now live and connected to your backend API!

