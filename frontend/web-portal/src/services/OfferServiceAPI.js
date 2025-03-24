/**
 * OfferServiceAPI.js
 * 
 * Provides functions to interact with the Offer Management Service.
 * Functions include retrieving composed offers based on search requests.
 */

import apiClient from './apiClient';

const OfferServiceAPI = {
  getOffer: async (params) => {
    try {
      return await apiClient.get('/api/offer', { params });
    } catch (error) {
      throw error;
    }
  },
};

export default OfferServiceAPI;
