FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/sreality_scraper
CMD ["scrapy", "crawl", "sreality"]
