import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join


class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join(", ")
    )


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()
