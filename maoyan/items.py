# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanIdItem(scrapy.Item):
    str = scrapy.Field()


class MaoyanItem(scrapy.Item):
    movieId = scrapy.Field()
    picture = scrapy.Field()
    name = scrapy.Field()
    name2 = scrapy.Field()
    type = scrapy.Field()
    place = scrapy.Field()
    length = scrapy.Field()
    time = scrapy.Field()
    description = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    # pictures = scrapy.Field()
    # videos = scrapy.Field()
