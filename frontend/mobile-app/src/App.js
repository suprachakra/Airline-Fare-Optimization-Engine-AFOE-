/**
 * App.js
 * 
 * Main React Native app component.
 * Sets up navigation (using React Navigation), global context providers, and initializes push notifications.
 */

import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen';
import DashboardScreen from './screens/DashboardScreen';
import { initPushNotifications } from './services/PushNotifications';

const Stack = createStackNavigator();

const App = () => {
  useEffect(() => {
    // Initialize push notifications on app startup
    initPushNotifications();
  }, []);

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} options={{ headerShown: false }}/>
        <Stack.Screen name="Dashboard" component={DashboardScreen} options={{ title: 'Dashboard' }}/>
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
