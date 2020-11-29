from ..items import HallIdItem
import scrapy


class HallSpider(scrapy.Spider):
    name = 'hall'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/cinemas?offset=0',
                  'https://maoyan.com/cinemas?offset=12',
                  'https://maoyan.com/cinemas?offset=24',
                  'https://maoyan.com/cinemas?offset=36',
                  'https://maoyan.com/cinemas?offset=48',
                  'https://maoyan.com/cinemas?offset=60',
                  'https://maoyan.com/cinemas?offset=72',
                  'https://maoyan.com/cinemas?offset=84',
                  'https://maoyan.com/cinemas?offset=96',
                  'https://maoyan.com/cinemas?offset=108',
                  'https://maoyan.com/cinemas?offset=120'
                  ]

    def parse(self, response):
        item = HallIdItem()
        list = response.css('.cinema-cell a::attr(href)').extract()
        for i in list:
            item["hallId"] = i
            yield item
