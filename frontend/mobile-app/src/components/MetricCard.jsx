/**
 * MetricCard.jsx
 * 
 * Reusable component for displaying a key metric with an icon.
 * Accepts props for title, value, icon, and an optional subtitle.
 */

import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
import PropTypes from 'prop-types';

const MetricCard = ({ title, value, subtitle, icon }) => {
  return (
    <View style={styles.card}>
      {icon && <Image source={icon} style={styles.icon} />}
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.value}>{value}</Text>
      {subtitle && <Text style={styles.subtitle}>{subtitle}</Text>}
    </View>
  );
};

MetricCard.propTypes = {
  title: PropTypes.string.isRequired,
  value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
  subtitle: PropTypes.string,
  icon: PropTypes.any,
};

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    padding: 16,
    borderRadius: 8,
    elevation: 2,
    marginVertical: 8,
    alignItems: 'center',
  },
  icon: {
    width: 40,
    height: 40,
    marginBottom: 8,
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  value: {
    fontSize: 24,
    marginVertical: 4,
  },
  subtitle: {
    fontSize: 12,
    color: '#555',
  },
});

export default MetricCard;
