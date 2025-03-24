## Mobile App
The Mobile App is designed for managers and executives to monitor key metrics and receive real-time alerts on the go. Built with React Native, it provides a quick overview of dashboards, notifications, and real-time reports. This app focuses on ease of use, rapid access to critical data, and seamless integration with our backend APIs.


### Features
- **Real-Time Alerts:** Receive push notifications for significant events and threshold breaches.
- **Dashboard:** View key metrics such as current fares, demand forecasts, and revenue performance.
- **User Authentication:** Secure login to ensure only authorized users have access.
- **Quick Stats:** Instant overview of critical performance metrics.

### Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_org/AirlineFareOptimizationEngine.git
   cd AirlineFareOptimizationEngine/frontend/mobile-app
   ```
2. **Install Dependencies:**
   ```bash
   npm install
   ```
3. **Start the Development Server:**
   ```bash
   npm start
   ```
4. **Run on Device/Simulator:**
   - For Android: Use `npx react-native run-android`.
   - For iOS: Use `npx react-native run-ios` (macOS required).

### Folder Structure
- **android/**: Android-specific project files.
- **ios/**: iOS-specific project files.
- **src/**: Mobile app source code (React Native).
  - **components/**: Reusable UI components.
  - **screens/**: App screens for different views (Dashboard, Login).
  - **services/**: Modules for API calls and push notifications.
- **package.json**: Project dependencies and scripts.
- **Metro.config.js**: Configuration for the Metro bundler.
