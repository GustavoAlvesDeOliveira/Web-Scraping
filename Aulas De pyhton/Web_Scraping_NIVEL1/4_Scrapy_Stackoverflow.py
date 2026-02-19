from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Perguntas(Item):
    id = Field()
    pergunta = Field()
    #descricao = Field()

class StackOverFlowSpider(Spider):
    name = 'MeuPrimeiroSpider'
    custom_settings = {
    "ROBOTSTXT_OBEY": False,
    "DEFAULT_REQUEST_HEADERS": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
    },
    "USER_AGENT": "Mozilla/5.0"
    }

    start_urls = ['https://stackoverflow.com/questions']

    def parse(self, response):
        sel = Selector(response)
        perguntas = sel.xpath('//div[@id="questions"]//div[@class="bb bc-black-200"]')
        print(len(perguntas))
        for pergunta in perguntas:
            item = ItemLoader(item=Perguntas(), selector=pergunta)
            item.add_xpath('pergunta', './/h3/a/text()')
            #item.add_xpath('descricao', './/div[@class="s-post-summary--content-excerpt"]/text()')
            item.add_value('id', 1)

            yield item.load_item()


            

