# Dockerfile for Demand Forecasting Service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/

# Expose port (example: 5000)
EXPOSE 5000

ENV CONFIG_ENV=prod

# Run the forecasting service (adjust command as needed)
CMD ["python", "src/controllers/ForecastController.py"]
