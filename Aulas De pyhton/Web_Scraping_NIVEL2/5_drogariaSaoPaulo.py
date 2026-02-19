from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Farmacia(Item):
    nome = Field()
    Preco = Field()

class DrogariaSaoPauloCrawl(Spider):
    name = "DrogariaSaoPaulo"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/141.0.0.0 Safari/537.36',
    }

    allowed_domains = ['drogariasaopaulo.com.br']
    start_urls = ["https://www.drogariasaopaulo.com.br/pesquisa?q=shampoo&source=desktop"]

    def parse(self, response):
        produtos = response.xpath('//div[@class="card rnk-comp-card-shelf"]')

        for produto in produtos:
            item = ItemLoader(Farmacia(), produto)
            item.add_xpath('nome', './/div[@class="descricao-prateleira"]//a/text()')
            item.add_xpath('Preco', './/p[@class="price"]/text()')
            yield item.load_item()
