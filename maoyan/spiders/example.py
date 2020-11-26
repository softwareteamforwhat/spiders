from ..items import MaoyanIdItem
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']
    number=0
    def parse(self, response):
        item = MaoyanIdItem()
        id_list = response.css(
            'a[data-act="movies-click"]::attr(href)').extract()
        for i in id_list:
            if(len(i) > 6):
                item['str'] = i
                ExampleSpider.number+=1
                yield item
        base = 'https://maoyan.com/films?showType=3&offset='
        #先爬个五万个,两千个之后没得了
        if(ExampleSpider.number<50000):
            yield scrapy.Request(url=base+str(ExampleSpider.number), callback=self.parse)