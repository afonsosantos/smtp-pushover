# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./
COPY README.md README.md

# Install dependencies and the package itself
RUN poetry install

# Copy the application code
COPY smtp_pushover/ smtp_pushover/

# Expose the SMTP port
EXPOSE 1025

# Run the application using the entry point
CMD ["poetry", "run", "smtp-pushover"]
