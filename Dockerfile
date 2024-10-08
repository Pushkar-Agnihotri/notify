# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering output (helps with logging)
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "notify.py"]
