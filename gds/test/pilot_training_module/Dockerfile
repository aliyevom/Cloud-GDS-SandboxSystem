# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install SQLite (if not included in the base image)
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY . .

# Expose a port if the module needs to run a server (optional)
# EXPOSE 8080

# Command to run the training assessment
CMD ["python", "training_assessment.py"]
