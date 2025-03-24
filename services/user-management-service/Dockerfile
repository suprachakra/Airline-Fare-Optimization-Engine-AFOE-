# Dockerfile for User Management Service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose service port
EXPOSE 5003

ENV CONFIG_ENV=prod

# Run the User Management Service (adjust entrypoint as needed)
CMD ["python", "src/UserController.py"]
