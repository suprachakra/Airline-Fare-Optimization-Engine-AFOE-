/**
 * App.jsx
 * 
 * Main application component that sets up routing and context providers.
 * Uses React Router to define routes for Login, Dashboard, Pricing Controls, and Reports.
 */

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import PricingControlsPage from './pages/PricingControlsPage';
import ReportsPage from './pages/ReportsPage';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={LoginPage} />
        <Route path="/dashboard" component={DashboardPage} />
        <Route path="/pricing-controls" component={PricingControlsPage} />
        <Route path="/reports" component={ReportsPage} />
      </Switch>
    </Router>
  );
};

export default App;
