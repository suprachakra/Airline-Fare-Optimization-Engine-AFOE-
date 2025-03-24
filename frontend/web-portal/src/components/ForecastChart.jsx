/**
 * ForecastChart.jsx
 * 
 * Component to visualize demand forecasts vs. actual bookings.
 * Uses a charting library (e.g., Chart.js) to render line or bar charts.
 */

import React, { useEffect, useState } from 'react';
import ForecastServiceAPI from '../services/ForecastServiceAPI';
// Assuming a chart library is installed (e.g., react-chartjs-2)
import { Line } from 'react-chartjs-2';

const ForecastChart = () => {
  const [chartData, setChartData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchForecastData() {
      try {
        const data = await ForecastServiceAPI.getForecast({ route: "NYC-LON", date: "2023-06-05" });
        // Transform data for chart display
        const labels = data.timestamps;
        const forecast = data.forecasted_demand;
        const actual = data.actual_demand;
        setChartData({
          labels,
          datasets: [
            {
              label: 'Forecasted Demand',
              data: forecast,
              borderColor: 'rgba(75,192,192,1)',
              fill: false,
            },
            {
              label: 'Actual Demand',
              data: actual,
              borderColor: 'rgba(255,99,132,1)',
              fill: false,
            },
          ],
        });
      } catch (err) {
        setError(err.message);
      }
    }
    fetchForecastData();
  }, []);

  if (error) return <div>Error: {error}</div>;
  if (!chartData) return <div>Loading forecast data...</div>;

  return (
    <div>
      <h3>Demand Forecast vs Actual</h3>
      <Line data={chartData} />
    </div>
  );
};

export default ForecastChart;
