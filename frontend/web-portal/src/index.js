/**
 * index.js
 * 
 * Entry point for the web application.
 * Bootstraps the React app by rendering the App component into the root element.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles/main.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
