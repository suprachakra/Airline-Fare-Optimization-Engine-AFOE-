/**
 * config.js
 * Holds configuration parameters for the PSS integration module.
 *
 * Variables include:
 * - API_ENDPOINT: Base URL for the Amadeus PSS API.
 * - API_KEY: Secret key for authentication.
 * - TIMEOUT: Request timeout settings.
 *
 * In a production environment, these should be loaded from environment variables or a secure config service.
 */

module.exports = {
  API_ENDPOINT: process.env.PSS_API_ENDPOINT || "https://api.amadeuspss.com",
  API_KEY: process.env.PSS_API_KEY || "YOUR_PSS_API_KEY_HERE",
  TIMEOUT: process.env.PSS_TIMEOUT || 5000 // in milliseconds
};
