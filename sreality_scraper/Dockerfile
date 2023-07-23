FROM python:3.7

WORKDIR /app

# Copy only the necessary files for the sreality_scraper service
COPY . /app

# Install the required Python dependencies for the sreality_scraper service
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Scrapy project files (e.g., scrapy.cfg)
WORKDIR /app/sreality_scraper

# Replace "your_scrapy_crawl_command" with the actual command to run your Scrapy spider
CMD ["scrapy", "crawl", "sreality"]
