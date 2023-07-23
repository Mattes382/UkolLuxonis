FROM python:3.7

# Set the working directory to /app/web
WORKDIR /app/web

# Copy only the necessary files for the web service
COPY requirements.txt .

# Install the required Python dependencies for the web service
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main web application file (e.g., app.py)
COPY app.py .
COPY ./templates/ /app/web/templates/

# Replace "your_web_crawl_command" with the actual command to run your web application
CMD ["python", "app.py"]
