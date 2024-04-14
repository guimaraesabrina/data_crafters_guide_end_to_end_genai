# Use the official Python 3.10 slim image from Docker Hub as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file first, to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the working directory
COPY . .

# Set environment variables to run Uvicorn in production
ENV UVICORN_HOST=0.0.0.0 UVICORN_PORT=8000

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.backend.crafter:app", "--host", "0.0.0.0", "--port", "8000"]

