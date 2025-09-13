# Quick Deployment Setup Guide

## 🚀 Complete Deployment Checklist

### Backend (Render) - COMPLETED ✅
- [x] `requirements.txt` - Python dependencies
- [x] `Dockerfile` - Container configuration
- [x] `README_BACKEND.md` - Step-by-step Render deployment guide

### Frontend (Vercel) - COMPLETED ✅
- [x] `static/config.js` - Configurable backend URL
- [x] `vercel.json` - Vercel deployment configuration
- [x] `env.example` - Environment variables template
- [x] `README_FRONTEND.md` - Step-by-step Vercel deployment guide
- [x] Updated `templates/index.html` - Now uses configurable API URL

## 📋 Deployment Order

### 1. Deploy Backend First (Render)
1. Push your code to GitHub
2. Follow `README_BACKEND.md` instructions
3. Get your Render backend URL (e.g., `https://your-app.onrender.com`)

### 2. Update Frontend Configuration
1. Open `static/config.js`
2. Replace `https://your-backend-app.onrender.com` with your actual Render URL
3. Commit and push changes

### 3. Deploy Frontend (Vercel)
1. Follow `README_FRONTEND.md` instructions
2. Get your Vercel frontend URL (e.g., `https://your-app.vercel.app`)

## 🔧 Quick Configuration Update

After deploying your backend, update the frontend configuration:

```javascript
// In static/config.js
const config = {
  // Replace with your actual Render backend URL
  API_URL: 'https://your-actual-backend-name.onrender.com',
  // ... rest stays the same
};
```

## 🎯 Final Result

- **Backend**: `https://your-backend.onrender.com` (serves ML predictions)
- **Frontend**: `https://your-frontend.vercel.app` (serves the UI)
- **Connection**: Frontend automatically calls backend API for predictions

## 📚 Documentation

- **Backend Deployment**: See `README_BACKEND.md`
- **Frontend Deployment**: See `README_FRONTEND.md`
- **Troubleshooting**: Both READMEs include common issues and solutions

## ⚠️ Important Notes

1. **Free Tier Limitations**:
   - Render: App sleeps after 15min inactivity (cold start ~30s)
   - Vercel: No sleep mode, but 100GB bandwidth limit

2. **CORS**: If you get CORS errors, add `flask-cors` to your backend

3. **Model File**: Ensure `grape_disease_classifier.h5` is in your repository

4. **Testing**: Always test locally before deploying

Your deployment files are ready! Follow the README guides for step-by-step deployment instructions.
