/**
 * PricingServiceAPI.js
 * 
 * Provides functions to interact with the Pricing Service API endpoints.
 * Functions include retrieving fares and submitting manual override requests.
 */

import apiClient from './apiClient';

const PricingServiceAPI = {
  getFares: async () => {
    // Example: GET request to fetch current pricing data
    try {
      return await apiClient.get('/api/pricing/fares');
    } catch (error) {
      throw error;
    }
  },
  submitOverride: async (overrideData) => {
    // Example: POST request to submit a manual pricing override
    try {
      return await apiClient.post('/api/pricing/override', overrideData);
    } catch (error) {
      throw error;
    }
  },
};

export default PricingServiceAPI;
