# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Install gunicorn
RUN gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
