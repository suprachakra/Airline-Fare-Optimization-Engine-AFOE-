/**
 * PricingControlsPage.jsx
 * 
 * Page for manual overrides or adjustments to pricing.
 * Provides a form to input override values and review system recommendations.
 */

import React, { useState } from 'react';
import PricingServiceAPI from '../services/PricingServiceAPI';

const PricingControlsPage = () => {
  const [flightId, setFlightId] = useState('');
  const [overrideFare, setOverrideFare] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleOverride = async (e) => {
    e.preventDefault();
    try {
      const response = await PricingServiceAPI.submitOverride({ flightId, overrideFare });
      setResult(response);
      setError('');
    } catch (err) {
      setError("Error submitting override: " + err.message);
      setResult(null);
    }
  };

  return (
    <div className="pricing-controls-page">
      <h1>Pricing Controls</h1>
      <form onSubmit={handleOverride}>
        <label>
          Flight ID:
          <input type="text" value={flightId} onChange={(e) => setFlightId(e.target.value)} required />
        </label>
        <label>
          Override Fare:
          <input type="number" value={overrideFare} onChange={(e) => setOverrideFare(e.target.value)} required />
        </label>
        <button type="submit">Submit Override</button>
      </form>
      {error && <div className="error-message">{error}</div>}
      {result && <div className="result-message">Override successful: {JSON.stringify(result)}</div>}
    </div>
  );
};

export default PricingControlsPage;
