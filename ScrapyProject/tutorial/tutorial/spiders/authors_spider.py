import scrapy
from tutorial.items import AuthorItem
from tutorial.loaders import AuthorLoader


class AuthorSpider(scrapy.Spider):
    name = "author"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    @staticmethod
    def parse_author(response):
        loader = AuthorLoader(item=AuthorItem(), response=response)
        loader.add_css("name", "h3.author-title::text")
        loader.add_css("birthdate", ".author-born-date::text")
        loader.add_css("bio", ".author-description::text")
        yield loader.load_item()
