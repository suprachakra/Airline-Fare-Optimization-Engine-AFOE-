/**
 * LoginScreen.jsx
 * 
 * Screen for user login on the mobile app.
 * Provides form inputs for username and password and calls the backend API for authentication.
 */

import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import ApiService from '../services/ApiService';
import { useNavigation } from '@react-navigation/native';

const LoginScreen = () => {
  const navigation = useNavigation();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      const response = await ApiService.post('/api/user/login', { username, password });
      if (response.token) {
        // Save token in local storage or secure store (for demonstration, using local storage)
        // In production, use secure storage for mobile apps.
        // AsyncStorage is recommended for React Native.
        navigation.navigate('Dashboard');
      } else {
        setError("Invalid credentials.");
      }
    } catch (err) {
      setError("Login error: " + err.message);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Login</Text>
      {error !== '' && <Text style={styles.error}>{error}</Text>}
      <TextInput 
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
      />
      <TextInput 
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#fff',
    justifyContent: 'center',
  },
  header: {
    fontSize: 24,
    marginBottom: 24,
    textAlign: 'center',
  },
  input: {
    borderColor: '#ccc',
    borderWidth: 1,
    marginBottom: 16,
    padding: 8,
    borderRadius: 4,
  },
  error: {
    color: 'red',
    marginBottom: 16,
    textAlign: 'center',
  }
});

export default LoginScreen;
