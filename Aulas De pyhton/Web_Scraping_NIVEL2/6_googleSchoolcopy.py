from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Artigo(Item):
    titulo = Field()
    citacoes = Field()
    autores = Field()
    url = Field()

class GoogleScholar(Spider):
    name = "GoogleScholar"
    custom_settings = {
      'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    }

    allowed_domains = ['scholar.google.com']
    start_urls = ['https://scholar.google.com/scholar?as_ylo=2023&q=AI&hl=en&as_sdt=0,5']

    download_delay = 2

    
    def parse(self, response):
        print(response.text[:1000])

        sel = Selector(response)

        artigos = sel.xpath("//div[@class='gs_ri']")

        for artigo in artigos:
            item = ItemLoader(Artigo(), artigo)

            titulo = artigo.xpath('.//h3/a//text()').get()
            item.add_value('titulo', titulo)

            url = artigo.xpath('.//h3/a/@href').get()
            item.add_value('url', url)

            autores = artigo.xpath('.//div[@class="gs_a"]//text()').getall()
            autores = "".join(autores)
            autores = autores.split('-')[0].strip()

            item.add_value('autores', autores)
            try:
                citacoes = artigo.xpath('.//a[contains(@href,"cites")]/text()').get()
                citacoes = citacoes.replace('Cited by', '')
            except:
                pass

            item.add_value('citacoes',citacoes)
            yield item.load_item()