# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies for telemetry or external integrations
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

# Copy source code
COPY . .

# Expose ports if needed (e.g., for telemetry or monitoring services)
EXPOSE 8080

# Command to run the simulator
CMD ["python", "simulator.py"]
