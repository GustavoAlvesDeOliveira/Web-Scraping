from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess


class Artigo(Item):
    titulo = Field()
    preco = Field()
    descricao = Field()


class MercadoLivreCrawler(CrawlSpider):
    name = 'MercadoLivre'

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0 Safari/537.36",
        "CLOSESPIDER_PAGECOUNT": 20,
        "DOWNLOAD_DELAY": 1,
        "COOKIES_ENABLED": True
    }

    allowed_domains = ['mercadolivre.com.br']

    start_urls = ['https://lista.mercadolivre.com.br/notebook']

    rules = (
        Rule(
            LinkExtractor(allow=r'_Desde_\d+'),
            follow=True
        ),
        Rule(
            LinkExtractor(allow=r'/p/'),
            callback='parse_items',
            follow=True
        ),
    )


    def parse_items(self, response):
        item = ItemLoader(Artigo(), response)
        print("ENTROU NO PRODUTO:", response.url)

        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descricao', '//p[@class="ui-pdp-description__content"]/text()')
        item.add_xpath('preco', '//span[@class="andes-money-amount__fraction"]/text()')

        yield item.load_item()


processo = CrawlerProcess({
    'FEEDS': {
        'mercadolivre.csv': {'format': 'csv'}
    }
})

processo.crawl(MercadoLivreCrawler)
processo.start()
