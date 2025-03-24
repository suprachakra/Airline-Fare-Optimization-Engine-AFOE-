/**
 * ApiService.js
 * 
 * Handles API calls to backend services from the mobile app.
 * Configures a base URL, attaches authentication tokens if needed,
 * and provides standardized error handling.
 */

import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000',
  timeout: 5000,
});

// Request interceptor to attach auth token if available
apiClient.interceptors.request.use(
  (config) => {
    // For mobile, consider using AsyncStorage for tokens
    // For demonstration, we use a placeholder
    const token = null; // Replace with token retrieval logic
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.error('API Error:', error.response || error.message);
    return Promise.reject(error);
  }
);

export default apiClient;
