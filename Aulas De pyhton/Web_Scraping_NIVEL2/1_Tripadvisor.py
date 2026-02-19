from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from itemloaders.processors import MapCompose
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess

class Hotel(Item):
    nome = Field()
    preco = Field()
    descricao = Field()


class TripAdvisorSpider(CrawlSpider):
    name = 'TripAdvisor'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",

        "DEFAULT_REQUEST_HEADERS": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
        },

        "DOWNLOAD_DELAY": 2,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "COOKIES_ENABLED": True
    }


    start_urls = ['https://www.tripadvisor.com.br/Hotels-g28953-New_York-Hotels.html']



    rules = (
        Rule(
            LinkExtractor(
                allow=r'/Hotel_Review-'
            ), follow=True, callback="parse_hotel"
        ),
    )

    def parse_hotel(self, response):
        sel = Selector(response)
        item = ItemLoader(Hotel(), sel)

        item.add_xpath('nome', '//h1[@id="HEADING"]/text()')
        item.add_xpath('preco', '//div[@class="gJKlf"]/text()')
        item.add_xpath('descricao', '//div[@class="fIrGe _T"]/text()')

        yield item.load_item()