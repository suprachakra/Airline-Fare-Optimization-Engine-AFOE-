/**
 * index.js
 * Main integration logic for Amadeus PSS.
 * - Initializes connection with PSS.
 * - Authenticates using credentials from config.
 * - Routes incoming API requests to appropriate helper functions.
 *
 * This module is built to be highly resilient with automatic retries and proper logging.
 */

const config = require('./config');
const helpers = require('./helpers');
const errorHandler = require('./errorHandler');
const logger = require('./logger');

// Example function to initialize connection to PSS
async function initPSSConnection() {
  try {
    logger.info("Initializing connection to Amadeus PSS...");
    // Here we simulate an authentication call to the PSS system using config parameters.
    const authToken = await helpers.authenticate(config.API_ENDPOINT, config.API_KEY);
    logger.info("Successfully authenticated with Amadeus PSS.");
    return authToken;
  } catch (error) {
    errorHandler.handleError(error, "initPSSConnection");
    throw error;
  }
}

// Example API endpoint handler
async function getBookingData(requestParams) {
  try {
    // Validate request parameters using helper functions
    helpers.validateRequest(requestParams);
    // Get data from PSS
    const data = await helpers.fetchBookingData(config.API_ENDPOINT, requestParams);
    return data;
  } catch (error) {
    errorHandler.handleError(error, "getBookingData");
    throw error;
  }
}

module.exports = {
  initPSSConnection,
  getBookingData
};
