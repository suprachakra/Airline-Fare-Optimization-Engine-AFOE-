/**
 * DashboardPage.jsx
 * 
 * Main dashboard page aggregating key information and alerts.
 * It includes components like PricingDashboard, ForecastChart, etc.
 */

import React from 'react';
import PricingDashboard from '../components/PricingDashboard';
import ForecastChart from '../components/ForecastChart';

const DashboardPage = () => {
  return (
    <div className="dashboard-page">
      <h1>Dashboard</h1>
      <PricingDashboard />
      <ForecastChart />
      {/* Additional components and alerts can be added here */}
    </div>
  );
};

export default DashboardPage;
