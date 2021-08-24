import scrapy
from ..items import GoogleItem



class QuotesSpider(scrapy.Spider):
    name = "google"
    # urls = [
    #          'https://www.google.com/search?q=python',
    #      ]
    def start_requests(self):
        urls = [
            'https://www.google.com/search?q=python',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):


        items = GoogleItem()

        name = response.xpath("//cite[@class='iUh30 Zu0yb tjvcx']/text()").extract()
        first = response.xpath("//h3[@class='LC20lb DKV0Md']/text()").extract()

        items['name'] = name,
        items['title'] = first,

        yield items
        print(items)
