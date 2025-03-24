# Dockerfile for Network Planning & Codeshare Service
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose port (if needed)
EXPOSE 5000

ENV CONFIG_ENV=prod

# Run the service (for example, starting the ScheduleImporter)
CMD ["python", "src/ScheduleImporter.py"]
