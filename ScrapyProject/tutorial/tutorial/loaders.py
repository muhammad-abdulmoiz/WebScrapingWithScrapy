from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


class AuthorLoader(ItemLoader):
    default_output_processor = TakeFirst()

    name_in = MapCompose(str.strip, str.title)
    birthdate_in = MapCompose(str.strip)
    bio_in = MapCompose(str.strip)
