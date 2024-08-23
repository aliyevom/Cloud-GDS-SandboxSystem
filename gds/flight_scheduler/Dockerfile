# Base image for Python
FROM python:3.9-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the necessary port
EXPOSE 50051

# Run the scheduler as the entry point
CMD ["python", "scheduler.py"]
