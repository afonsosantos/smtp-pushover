# Use an official Python runtime as a base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the SMTP port
EXPOSE 1025

# Run the application
CMD ["python", "main.py"]
