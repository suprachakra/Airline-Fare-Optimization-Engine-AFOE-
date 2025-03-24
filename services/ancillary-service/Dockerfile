# Dockerfile for Ancillary & Merchandising Service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose the service port
EXPOSE 5001

# Set default environment variable
ENV CONFIG_ENV=prod

# Command to run the ancillary service (adjust entrypoint as needed)
CMD ["python", "src/controllers/AncillaryController.py"]
