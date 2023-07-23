import scrapy
from ..items import SrealityScraperItem


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    base_url = 'https://www.sreality.cz/api/cs/v2/estates'
    items_per_page = 100
    max_pages = 5

    def start_requests(self):
        for page in range(1, self.max_pages + 1):
            url = f'{self.base_url}?category_main_cb=1&category_type_cb=1&sort=0&per_page={self.items_per_page}&page={page}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
         jsonresponse = response.json()
         for item in jsonresponse["_embedded"]['estates']:
             yield scrapy.Request( 'https://www.sreality.cz/api' + item['_links']['self']['href'] ,
                          callback=self.parse_flat)

    def parse_flat(self, response):
        jsonresponse = response.json()
        flat = SrealityScraperItem()
        flat['title'] = jsonresponse['name']['value']

        for images in jsonresponse['_embedded']['images']:
            if images['_links']['dynamicDown']:
                tmp = images['_links']['dynamicDown']['href'].replace('{width}', '400')
                tmp = tmp.replace('{height}', '300')
                flat['image_url'] = tmp
                break

        yield flat

