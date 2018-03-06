# -*- coding: utf-8 -*-
import scrapy
from tibia.items import TibiaItem

class TibiabotSpider(scrapy.Spider):
    name = 'top300all'
    allowed_domains = ['www.secure.tibia.com']
    start_urls = [
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage={0}'.format(page) for page in range(1,13)
        ]
        
    custom_settings = {
    	'FEED_URI' : 'tmp/top300all.csv'
    }

    def parse(self, response):
        #table = response.xpath("//table").extract()
        #rank = response.xpath("//table/tr/td[1]/text()").extract()
        scrapedItem = TibiaItem()
        
        scrapedItem["name"] = response.xpath("//table/tr/td/a/text()").extract()
        scrapedItem["vocation"] = response.xpath("//table/tr/td[3][not(contains(text(), 'Vocation'))]/text()").extract()
        scrapedItem["level"] = response.xpath("//table/tr/td[4][not(contains(text(), 'Level'))]/text()").extract()
        scrapedItem["exp"] = response.xpath("//table/tr/td[5][not(contains(text(), 'Points'))]/text()").extract()
        
        for item in zip(scrapedItem["name"],scrapedItem["vocation"],scrapedItem["level"],scrapedItem["exp"]):
            scraped_info = {
                "name" : item[0],
                "vocation" : item[1],
                "level" : item[2],
                "exp" : item[3]
            }
            yield scraped_info
            #yield scrapedItem
        
        # not working atm, it goes to first link (when statring on page 1 it goes to 2, 
        # but on page 2 it goes to 1 again since it only extracts first link)
        next_page = response.xpath("//b/a/@href").extract()
        
        #if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse, dont_filter = True)