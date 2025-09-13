// Configuration file for backend API URL
// This makes it easy to update the backend URL without rebuilding

const config = {
  // Backend API URL - Update this with your Railway backend URL
  API_URL: 'https://your-railway-app.railway.app',
  
  // For development (uncomment and comment out the above line)
  // API_URL: 'http://localhost:5000',
  
  // API endpoints
  ENDPOINTS: {
    PREDICT: '/predict',
    HOME: '/'
  }
};

// Make config available globally
window.APP_CONFIG = config;

