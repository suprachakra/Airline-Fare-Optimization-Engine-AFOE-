/**
 * ForecastServiceAPI.js
 * 
 * Provides functions to interact with the Forecasting Service API endpoints.
 * Functions include retrieving demand forecasts for given routes/dates.
 */

import apiClient from './apiClient';

const ForecastServiceAPI = {
  getForecast: async (params) => {
    try {
      return await apiClient.get('/api/forecast', { params });
    } catch (error) {
      throw error;
    }
  },
};

export default ForecastServiceAPI;
