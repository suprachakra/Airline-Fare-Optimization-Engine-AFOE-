/**
 * PricingDashboard.jsx
 * 
 * Dashboard component displaying current pricing data, recommendations, and performance metrics.
 * This component fetches data via the PricingServiceAPI and displays charts/tables.
 */

import React, { useEffect, useState } from 'react';
import PricingServiceAPI from '../services/PricingServiceAPI';
import './Dashboard.module.css'; // Scoped styles

const PricingDashboard = () => {
  const [pricingData, setPricingData] = useState(null);
  const [error, setError] = useState(null);

  // Fetch pricing data on component mount
  useEffect(() => {
    async function fetchData() {
      try {
        const data = await PricingServiceAPI.getFares();
        setPricingData(data);
      } catch (err) {
        setError(err.message);
      }
    }
    fetchData();
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }
  if (!pricingData) {
    return <div>Loading pricing data...</div>;
  }

  return (
    <div className="pricing-dashboard">
      <h2>Current Pricing Dashboard</h2>
      {/* Render pricing data in a table or chart */}
      <table>
        <thead>
          <tr>
            <th>Flight</th>
            <th>Fare</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {pricingData.map((item, index) => (
            <tr key={index}>
              <td>{item.flight}</td>
              <td>{item.fare}</td>
              <td>{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default PricingDashboard;
