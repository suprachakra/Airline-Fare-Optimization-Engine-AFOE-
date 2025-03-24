/**
 * LoginPage.jsx
 * 
 * Login screen for user authentication.
 * Contains form fields for username and password, and calls the user management API for login.
 */

import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import apiClient from '../services/apiClient';

const LoginPage = () => {
  const history = useHistory();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await apiClient.post('/api/user/login', { username, password });
      if (response.token) {
        // Save token (e.g., in localStorage)
        localStorage.setItem('authToken', response.token);
        history.push('/dashboard');
      } else {
        setError("Login failed. Please check your credentials.");
      }
    } catch (err) {
      setError("Login error: " + err.message);
    }
  };

  return (
    <div className="login-page">
      <h2>Login</h2>
      {error && <div className="error-message">{error}</div>}
      <form onSubmit={handleLogin}>
        <label>
          Username:
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            required 
          />
        </label>
        <label>
          Password:
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
        </label>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
