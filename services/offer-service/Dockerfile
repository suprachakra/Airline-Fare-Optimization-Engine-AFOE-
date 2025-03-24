# Dockerfile for Offer Management Service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose service port
EXPOSE 5002

ENV CONFIG_ENV=prod

# Command to run the offer service (adjust entrypoint as needed)
CMD ["python", "src/controllers/OfferController.py"]
