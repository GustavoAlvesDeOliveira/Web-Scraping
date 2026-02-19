from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Artigo(Item):
    titulo = Field()
    conteudo = Field()
    ordem = Field()


class Video(Item):
    titulo = Field()
    ficha = Field()
    ordem = Field()

class IGNCrawler(CrawlSpider):
    name = 'ign'
    contador = 0
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
      'CLOSESPIDER_PAGECOUNT': 20, 
      'FEED_EXPORT_FIELDS': ['ordem','titulo', 'ficha', 'conteudo'],
      'FEED_EXPORT_ENCODING': 'utf-8'
    }

    allowed_domains = ['br.ign.com']
    start_urls = ['https://br.ign.com/se/?model=&q=ps5']

    download_delay = 1

    rules = (
        Rule(
            LinkExtractor(
                allow=r'type='
            ), follow=True), 
        Rule(LinkExtractor(
            allow=r'&page=\d+'
            ), follow=True), 
        
        Rule(
            LinkExtractor(
                allow=r'/video/',
                deny=r'utm_source=recirc',
            ), follow=True, callback='parse_video'),
        Rule(
            LinkExtractor(
                allow=r'/news/',
                deny=r'utm_source=recirc',
            ), follow=True, callback='parse_news'),
    )


    # VIDEO
    def parse_video(self, response):
        self.contador += 1
        item = ItemLoader(Video(), response)
        item.add_value('ordem', self.contador)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('ficha', '//span[@class="publish-date"]/text()')
        yield item.load_item()

    # ARTICULO
    def parse_news(self, response):
        self.contador += 1
        item = ItemLoader(Artigo(), response)
        item.add_value('ordem', self.contador)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('conteudo', '//div[@id="id_text"]//*/text()')
        yield item.load_item()
