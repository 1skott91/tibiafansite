# -*- coding: utf-8 -*-
import scrapy


class TibiabotSpider(scrapy.Spider):
    name = 'top300all'
    allowed_domains = ['www.secure.tibia.com']
    start_urls = [
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=1/',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=2',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=3',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=4',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=5',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=6',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=7',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=8',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=9',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=10',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=11',
        'https://secure.tibia.com/community/?subtopic=highscores&world=Damora&list=experience&profession=0&currentpage=12'
        ]
    custom_settings = {
    	'FEED_URI' : 'tmp/top300all.csv'
    }

    def parse(self, response):
        #table = response.xpath("//table").extract()
        #rank = response.xpath("//table/tr/td[1]/text()").extract()
        name = response.xpath("//table/tr/td/a/text()").extract()
        vocation = response.xpath("//table/tr/td[3][not(contains(text(), 'Vocation'))]/text()").extract()
        level = response.xpath("//table/tr/td[4][not(contains(text(), 'Level'))]/text()").extract()
        exp = response.xpath("//table/tr/td[5][not(contains(text(), 'Points'))]/text()").extract()
            
        for item in zip(name,vocation,level,exp):
            scraped_info = {
                "name" : item[0],
                "vocation" : item[1],
                "level" : item[2],
                "exp" : item[3]
            }
            yield scraped_info
        
        # not working atm, it goes to first link (when statring on page 1 it goes to 2, 
        # but on page 2 it goes to 1 again since it only extracts first link)
        '''next_page = response.xpath("//b/a/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter = True)'''