# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy necessary docs
COPY requirements.txt set_envvars.sh kickoff.sh ./

# Install any dependencies (if you have a requirements file)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=src/pps.py
ENV FLASK_RUN_HOST=0.0.0.0
