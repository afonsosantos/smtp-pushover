# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the application code
COPY smtp_pushover/ smtp_pushover/

# Expose the SMTP port
EXPOSE 1025

# Run the application
CMD ["poetry", "run", "smtp-pushover"]
