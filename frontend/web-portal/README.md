## Web Portal
The Web Portal is an internal web application designed for airline analysts and operations teams. It provides dashboards for real-time pricing, demand forecasting, offer management, and reporting. The portal allows users to:
- View dynamic pricing and revenue metrics.
- Monitor demand forecasts and inventory updates.
- Manually adjust pricing controls.
- Generate detailed analytical reports.

### Features
- **Dashboard:** Aggregates key metrics and performance indicators.
- **Login:** Secure authentication for internal users.
- **Pricing Controls:** Interface for manual pricing overrides and rule adjustments.
- **Reports:** Detailed analysis of revenue performance and forecast accuracy.

### Development Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_org/AirlineFareOptimizationEngine.git
   cd AirlineFareOptimizationEngine/frontend/web-portal
   ```
2. **Install Dependencies:**
   ```bash
   npm install
   ```
3. **Start the Development Server:**
   ```bash
   npm start
   ```
4. **Build for Production:**
   ```bash
   npm run build
   ```

### Folder Structure
- `public/`: Static assets including the HTML template and favicon.
- `src/`: Contains the React source code including components, pages, services, and styles.
- `package.json`: Lists dependencies and scripts.
- `webpack.config.js`: Configuration for bundling the web portal.
