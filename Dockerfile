# Dockerfile for the web service
# Use a base image with Python and Flask installed
FROM python:3.7

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 8080

# Define the command to run the Flask application
CMD ["python", "app.py"]
