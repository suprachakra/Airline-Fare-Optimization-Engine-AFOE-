# Dockerfile for Amadeus PSS Integration Service

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose port (if needed, e.g., if service exposes an API)
EXPOSE 5000

# Define default environment variables (can also be provided via .env)
ENV CONFIG_ENV=prod

# Command to run the PSS integration service (for example, running InventorySyncJob)
CMD ["python", "src/InventorySyncJob.py"]
