/**
 * DashboardScreen.jsx
 * 
 * Displays summary metrics and recent alerts for a quick overview.
 * Combines various MetricCard components to present key performance indicators.
 */

import React, { useEffect, useState } from 'react';
import { View, ScrollView, StyleSheet, Text } from 'react-native';
import MetricCard from '../components/MetricCard';
import ApiService from '../services/ApiService';

const DashboardScreen = () => {
  const [metrics, setMetrics] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchMetrics() {
      try {
        const data = await ApiService.get('/api/dashboard/metrics');
        setMetrics(data);
      } catch (err) {
        setError(err.message);
      }
    }
    fetchMetrics();
  }, []);

  if (error) return <Text style={styles.errorText}>Error: {error}</Text>;
  if (!metrics) return <Text style={styles.loadingText}>Loading metrics...</Text>;

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.header}>Dashboard</Text>
      <MetricCard title="Current Fare" value={`$${metrics.currentFare}`} subtitle="Dynamic Pricing" />
      <MetricCard title="Forecasted Demand" value={metrics.forecastedDemand} subtitle="Bookings Expected" />
      <MetricCard title="Ancillary Revenue" value={`$${metrics.ancillaryRevenue}`} subtitle="Today" />
      {/* Add additional MetricCards as needed */}
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: '#f4f4f4',
    alignItems: 'center',
  },
  header: {
    fontSize: 24,
    marginVertical: 16,
  },
  loadingText: {
    fontSize: 16,
    marginTop: 50,
  },
  errorText: {
    fontSize: 16,
    marginTop: 50,
    color: 'red',
  },
});

export default DashboardScreen;
