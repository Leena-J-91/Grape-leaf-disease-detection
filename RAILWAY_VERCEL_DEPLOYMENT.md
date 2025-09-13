# Railway + Vercel Deployment Guide

## 🏗️ Architecture
- **Backend (ML API)**: Railway - Handles image processing and ML predictions
- **Frontend (UI)**: Vercel - Serves the web interface

## 🚀 Step-by-Step Deployment

### Part 1: Deploy Backend on Railway

#### Step 1.1: Prepare Repository
```bash
git add .
git commit -m "Prepare for Railway + Vercel deployment"
git push origin main
```

#### Step 1.2: Deploy on Railway
1. **Go to** [railway.app](https://railway.app)
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**
6. **Railway will auto-detect Python and deploy**

#### Step 1.3: Get Railway URL
- After deployment, Railway will give you a URL like: `https://your-app-name.railway.app`
- **Copy this URL** - you'll need it for the frontend

### Part 2: Deploy Frontend on Vercel

#### Step 2.1: Update Frontend Config
1. **Open** `static/config.js`
2. **Replace** `https://your-railway-app.railway.app` with your actual Railway URL
3. **Save the file**

#### Step 2.2: Deploy on Vercel
1. **Go to** [vercel.com](https://vercel.com)
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Project Name**: `grape-disease-frontend`
5. **Framework Preset**: Other
6. **Click "Deploy"**

## 🔧 Configuration Files Created

### Railway Backend:
- `railway.json` - Railway configuration
- `Procfile` - Process definition
- `app.py` - Updated for Railway (port configuration)

### Vercel Frontend:
- `vercel.json` - Updated for frontend-only deployment
- `static/config.js` - Points to Railway backend

## 📁 Project Structure After Deployment

```
Your Repository:
├── app.py                    # Backend (deployed on Railway)
├── requirements.txt          # Backend dependencies
├── grape_disease_classifier.h5  # ML model
├── templates/
│   └── index.html           # Frontend (deployed on Vercel)
├── static/
│   ├── config.js            # API configuration
│   └── image3.jpeg          # Background image
├── railway.json             # Railway config
├── vercel.json              # Vercel config
└── Procfile                 # Railway process
```

## 🌐 Final URLs

- **Frontend**: `https://your-frontend.vercel.app`
- **Backend API**: `https://your-backend.railway.app`

## ✅ Testing Your Deployment

### Test Backend:
```bash
curl -X POST https://your-backend.railway.app/predict \
  -F "image=@test_image.jpg"
```

### Test Frontend:
1. Visit your Vercel URL
2. Upload a grape leaf image
3. Check if prediction works

## 🔄 Update Process

### To update backend:
1. Make changes to `app.py`
2. Push to GitHub
3. Railway auto-deploys

### To update frontend:
1. Make changes to `templates/` or `static/`
2. Push to GitHub
3. Vercel auto-deploys

## 🐛 Troubleshooting

### Backend Issues:
- Check Railway logs in dashboard
- Verify model file is uploaded
- Check Python dependencies

### Frontend Issues:
- Verify `config.js` has correct Railway URL
- Check browser console for API errors
- Test API endpoint directly

### CORS Issues:
If you get CORS errors, add this to `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

## 💰 Cost Considerations

- **Railway**: Free tier available, then pay-as-you-go
- **Vercel**: Free tier for static sites
- **Total**: Very affordable for small projects

## 🎯 Benefits of This Setup

1. **Scalability**: Each service scales independently
2. **Performance**: CDN for frontend, optimized backend
3. **Reliability**: If one service goes down, the other works
4. **Cost-effective**: Pay only for what you use
5. **Easy updates**: Deploy frontend and backend separately

## 📞 Support

If you encounter issues:
1. Check Railway logs for backend errors
2. Check Vercel logs for frontend errors
3. Test API endpoints directly
4. Verify configuration files
