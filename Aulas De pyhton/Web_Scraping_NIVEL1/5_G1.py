from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class Noticia(Item):
    titulo = Field()
    #descricao = Field()

class G1Spider(Spider):
    name = 'G1'
    custom_settings = {
    "USER_AGENT": "Mozilla/5.0"
    }

    start_urls = ['https://g1.globo.com/']

    def parse(self, response):
        sel = Selector(response)
        noticias = sel.xpath('//div[@class="feed-post bstn-item-shape type-materia"]')
        for noticia in noticias:
            item = ItemLoader(item=Noticia(), selector=noticia)
            item.add_xpath('titulo', './/h2/a/p/text()')
            #item.add_xpath('descricao', '')
            
            yield item.load_item()



#py -m scrapy runspider G1.py -O g1.csv
processo = CrawlerProcess({
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'g1.csv'
})

processo.crawl(G1Spider)
processo.start()
