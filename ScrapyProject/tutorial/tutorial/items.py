import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()