# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
#from alcaldes.items import alcaldesiItem

import scrapy

class alcaldesSPider(scrapy.Spider):

    name = 'alcaldes'
    item_count = 0
    allowed_domain = ['www.wikipedia.org']
    start_urls = ['https://es.wikipedia.org/wiki/Anexo:Resultados_de_las_elecciones_seccionales_de_Ecuador_de_2014#Alcaldes']

    def parse_item(self, response):
        #ml_item  = alcaldesiItem()

        for alcaldes in response.css('.mw-parser-output'):
            canton = alcaldes.xpath('//table[@class = "wikitable"]/tbody/tr/td[1]/a/text()').extract()
            nombre_candidato = alcaldes.xpath('//table[@class = "wikitable"]/tbody/tr/td[2]/text()').extract()
            partidos = alcaldes.xpath('//table[@class = "wikitable"]/tbody/tr/td[3]/a/text()').extract()
            yield {
                'canton': canton,
                'nombre_candidato' : nombre_candidato,
                'partidos': partidos,
            }

        #info de producto
        #ml_item['canton'] = response.xpath('//table[@class = "wikitable"]/tbody/tr/td[1]/a/text()').extract_first()
        #ml_item['nombre_candidato'] = response.xpath('//table[@class = "wikitable"]/tbody/tr/td[2]').extract_first()
        #ml_item['partido'] = response.xpath('//table[@class = "wikitable"]//tr/td[3]').extract_first()
        #yield ml_item


        #def parse(self, response):
        #for alcaldes in response.xpath('//table[@class = "wikitable"]'):
        #    yield {
        #        'canton': response.xpath('//tbody/tr/td[1]/a/text()').extract_first(),
        #        'nombre_candidato': response.xpath('//table[@class = "wikitable"]/tbody/tr/td[2]').extract_first(),
        #        'tags': quote.css('div.tags a.tag::text').extract(),
        #    }
