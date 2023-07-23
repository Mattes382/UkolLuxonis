import time

import psycopg2
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from psycopg2 import OperationalError


# SrealityScraperPipeline
class PostgresPipeline:
    def open_spider(self, spider):
        retries = 5
        retry_delay = 5

        for _ in range(retries):
            try:
                self.connection = psycopg2.connect(
                    host="postgres",
                    port="5432",
                    user="postgres",
                    password="yourpassword",
                    database="sreality"
                )
                self.cursor = self.connection.cursor()
                print("Successfully connected to PostgreSQL.")
                return
            except OperationalError as e:
                print("Error connecting to PostgreSQL:", e)
                time.sleep(retry_delay)

        raise Exception("Failed to establish connection to PostgreSQL after multiple retries.")

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        query = "INSERT INTO scraped_data (title, image_url) VALUES (%s, %s)"
        self.cursor.execute(query, (item['title'], item['image_url']))
        self.connection.commit()
        return item
