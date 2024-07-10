import scrapy
from tutorial.items import QuoteItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response, **kwargs):
        for quote in response.css("div.quote"):
            loader = ItemLoader(item=QuoteItem(), selector=quote)
            loader.add_css("text", "span.text::text")
            loader.add_css("author", "small.author::text")
            loader.add_css("tags", "div.tags a.tag::text")
            yield loader.load_item()
