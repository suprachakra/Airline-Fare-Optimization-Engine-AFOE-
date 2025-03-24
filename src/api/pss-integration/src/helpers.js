/**
 * helpers.js
 * Contains helper functions for making API calls to Amadeus PSS, formatting data, and retrying requests.
 *
 * Functions include:
 * - authenticate: To obtain a token from PSS.
 * - fetchBookingData: To retrieve booking and inventory data.
 * - validateRequest: To ensure request parameters meet expected formats.
 */

const axios = require('axios');
const logger = require('./logger');

async function authenticate(apiEndpoint, apiKey) {
  // Example: Call authentication endpoint to receive a token.
  try {
    logger.info("Authenticating with PSS API...");
    const response = await axios.post(`${apiEndpoint}/auth`, { apiKey });
    // Validate response status and structure
    if (response.status === 200 && response.data.token) {
      return response.data.token;
    } else {
      throw new Error("Authentication failed: Invalid response");
    }
  } catch (error) {
    logger.error("Authentication error: " + error.message);
    throw error;
  }
}

async function fetchBookingData(apiEndpoint, params) {
  // This function fetches booking/inventory data with retry logic.
  const maxRetries = 3;
  let attempts = 0;
  while (attempts < maxRetries) {
    try {
      logger.info(`Fetching booking data (Attempt ${attempts + 1})...`);
      const response = await axios.get(`${apiEndpoint}/booking`, { params });
      if (response.status === 200) {
        return response.data;
      } else {
        throw new Error(`Unexpected status code: ${response.status}`);
      }
    } catch (error) {
      attempts++;
      logger.warn(`Attempt ${attempts} failed: ${error.message}`);
      if (attempts >= maxRetries) {
        throw error;
      }
      // Wait for a short period before retrying (exponential backoff can be implemented)
      await new Promise(res => setTimeout(res, 1000 * attempts));
    }
  }
}

function validateRequest(params) {
  // Basic validation: ensure required fields are present
  if (!params || !params.flightNumber || !params.date) {
    throw new Error("Invalid request: 'flightNumber' and 'date' are required.");
  }
  // Additional validations can be added here
}

module.exports = {
  authenticate,
  fetchBookingData,
  validateRequest
};
