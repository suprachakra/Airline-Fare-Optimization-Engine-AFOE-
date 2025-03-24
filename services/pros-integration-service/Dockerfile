# Dockerfile for PROS O&D Integration Service
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose port if service exposes an API endpoint
EXPOSE 5000

ENV CONFIG_ENV=prod

# Run the PROS integration service (example: run a script that syncs data)
CMD ["python", "src/PROSClient.py"]
