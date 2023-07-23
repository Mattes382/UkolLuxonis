BOT_NAME = "sreality_scraper"

SPIDER_MODULES = ["sreality_scraper.spiders"]
NEWSPIDER_MODULE = "sreality_scraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Your User-Agent String Here"

LOG_LEVEL = 'DEBUG'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Set a download delay to avoid overwhelming the server (optional)
# DOWNLOAD_DELAY = 3

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure item pipelines
ITEM_PIPELINES = {
    "sreality_scraper.pipelines.PostgresPipeline": 300,
}

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
