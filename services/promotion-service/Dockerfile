# Dockerfile for Promotion & Campaign Service
FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose port for API access
EXPOSE 5002

ENV CONFIG_ENV=prod

# Run the Promotion Service (entrypoint can be adapted for a specific framework)
CMD ["python", "src/controllers/PromotionController.py"]
