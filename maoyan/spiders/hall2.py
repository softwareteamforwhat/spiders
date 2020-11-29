from ..items import HallItem
import scrapy
import pandas as pd
import numpy as np


class Hall2Spider(scrapy.Spider):
    name = 'hall2'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films/343012']
    csv_path = 'D:\\1code\\python\\maoyanspider\\maoyan\\id.csv'
    cols = [0]
    df = pd.read_csv(csv_path, usecols=cols)
    cinemas = list(np.array(df.values).flatten('F'))
    for i in range(0, 250):
        cinemas[i] = "https://maoyan.com"+cinemas[i]
    start_urls = cinemas
    # print(start_urls)

    def parse(self, response):
        item = HallItem()
        item['picture'] = response.css(
            '.avatar-shadow img::attr(src)').extract_first()
        item['name'] = response.css(
            '.cinema-brief-container h1::text').extract_first()
        item['address'] = response.css('.address ::text').extract_first()
        item['phone'] = response.css('.telphone ::text').extract_first()
        features = response.css('.feature')
        feature_list = []
        for f in features:
            feature_tag = f.xpath('./span/text()').extract_first()
            feature_text = f.xpath('./p/text()').extract_first()
            feature_list.append([feature_tag, feature_text])
        item['service'] = feature_list
        yield item
