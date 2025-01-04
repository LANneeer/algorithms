import uuid
from typing import Iterable

import scrapy
from scrapy import Request


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Special:Random']

    def start_requests(self) -> Iterable[Request]:
        for _ in range(300):
            yield scrapy.Request(self.start_urls[0], callback=self.parse, dont_filter=True)
        # for url in self.start_urls:
        #     yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        yield {
            'id': str(uuid.uuid4()),
            'url': response.url,
            'title': response.xpath('//*[@id="firstHeading"]/span/text()').get(),
            'category': response.xpath('//*[@id="mw-normal-catlinks"]/ul//a/text()').getall(),
            'content': ' '.join(response.xpath('//*[@id="bodyContent"]//p/text()').getall())
        }
