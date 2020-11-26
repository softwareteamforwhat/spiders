from ..items import MaoyanItem
import scrapy
import pandas as pd
import numpy as np


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films/343012']
    csv_path = 'D:\\1code\\python\\maoyanspider\\maoyan\\test.csv'
    cols = [0]
    index = 400
    df = pd.read_csv(csv_path, usecols=cols)
    movies = list(np.array(df.values).flatten('F'))
    # length = len(movies)
    # print(length)
    # print(movies[2009])

    def parse(self, response):
        item = MaoyanItem()
        item['movieId'] = str(
            MovieSpider.movies[MovieSpider.index]).split('/')[-1]
        MovieSpider.index += 1
        item['picture'] = response.css(
            '.avatar-shadow img::attr(src)').extract_first()
        item['name'] = response.css(
            '.movie-brief-container h1::text').extract_first()
        item['name2'] = response.css(
            '.movie-brief-container div::text').extract_first()
        item['type'] = response.css(
            '.movie-brief-container').xpath('./ul/li/a/text()').extract()
        _ = response.css('.movie-brief-container').xpath(
            './ul/li[2]/text()').extract_first().replace(" ", "").replace("/", "").split('\n')
        item['place'] = _[1]
        item['length'] = _[2]
        item['time'] = response.css(
            '.movie-brief-container').xpath('./ul/li[3]/text()').extract_first()

        item['description'] = response.css('.dra::text').extract_first()
        director_url = response.css('.celebrity').xpath(
            './a[1]/img[1]/@data-src').extract_first()
        director_name = response.css('.celebrity').xpath(
            './div/a/text()').extract_first().replace(' ', '').replace('\n', '')
        item['director'] = [director_url, director_name]
        actors = response.css('.actor')
        actor_list = []
        for a in actors:
            actor_url = a.xpath('./a/img/@data-src').extract_first()
            actor_name = a.xpath(
                './div/a/text()').extract_first().replace(' ', '').replace('\n', '')
            actor_role = a.xpath('./div/span/text()').extract_first()
            actor = [actor_url, actor_name, actor_role]
            actor_list.append(actor)
        item['actors'] = actor_list
        yield item
        base = 'https://maoyan.com'
        for i in range(401, 2010):
            yield scrapy.Request(url=base+str(MovieSpider.movies[i]), meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302]
            }, callback=self.parse)
