# Dockerfile for Dynamic Pricing Service
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ ./src/

# Expose port (example: 5000)
EXPOSE 5000

# Define default environment variables
ENV CONFIG_ENV=prod

# Run the pricing service (adjust the command based on your entrypoint)
CMD ["python", "src/controllers/PricingController.py"]
