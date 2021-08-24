import scrapy
from ..items import GoogleItem


class QuotesSpider(scrapy.Spider):
    name = 'google'
    urls = [
        'https://www.google.com/search?q=python&sxsrf=ALeKk03F-Bhk5NXVDsZsS8rKLPXt468vrg%3A1629810808105&source=hp&ei=ePAkYbDXA-e-0PEPmqGjgAo&iflsig=AINFCbYAAAAAYST-iG4CyIKApucI6Wu4xU8-I97ZvPCN&oq=python&gs_lcp=Cgdnd3Mtd2l6EAMyBggjECcQEzIECCMQJzIECCMQJzIHCAAQsQMQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoHCCMQ6gIQJzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgQILhBDOgUILhCABDoFCAAQgAQ6BwgAEIAEEAo6CggAEIAEEMkDEApQ_J4GWLeoBmCTrQZoAnAAeACAAXmIAZ0FkgEDNS4ymAEAoAEBsAEK&sclient=gws-wiz&ved=0ahUKEwiw84-y3snyAhVnHzQIHZrQCKAQ4dUDCAc&uact=5'
    ]

    def parse(self, response):
        items = GoogleItem()
        try:
            url = response.css('iUh30 Zu0yb qLRx3b tjvcx').css('::text').extract()
            title = response.css('LC20lb DKV0Md').css('::text').extract()
            description = response.css('VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf').css('::text').extract()

            items['url'] = url
            items['title'] = title
            items['description'] = description

            yield items
        except:
            print('jebac disa')
