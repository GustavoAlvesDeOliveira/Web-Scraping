import scrapy

class TesteSpider(scrapy.Spider):
    name = "teste"

    start_urls = ["https://example.com"]

    def parse(self, response):
        yield {"status": "rodando"}
