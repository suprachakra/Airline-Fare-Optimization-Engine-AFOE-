/**
 * Metro.config.js
 * 
 * Configuration file for the Metro bundler used in React Native.
 * Adjust settings as needed for asset resolution, transformer options, and custom configurations.
 */

const { getDefaultConfig } = require('metro-config');

module.exports = (async () => {
  const {
    resolver: { sourceExts, assetExts }
  } = await getDefaultConfig();
  return {
    transformer: {
      // Add any custom transformer options here
    },
    resolver: {
      assetExts: assetExts.filter(ext => ext !== 'svg'),
      sourceExts: [...sourceExts, 'jsx', 'js', 'json', 'ts', 'tsx']
    }
  };
})();
