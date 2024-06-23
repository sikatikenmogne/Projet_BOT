const path = require('path');

module.exports = {
  // Entry point of your application
  entry: './static/js/app.js', // Adjust this path to the main JS file of your Flask app

  // Output configuration
  output: {
    filename: 'bundle.js', // The name of the bundled file
    path: path.resolve(__dirname, 'static/dist'), // The output directory
  },

  // Target configuration
  target: 'web', // Ensures compatibility with web browsers

  // Mode
  mode: 'development', // Use 'production' for production builds
};