# -*- coding: utf8 -*-
import scrapy
import re
import csv

from ScrapyRadio_SansEnv.items import ScrapyRadioItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest
from scrapy import log

class MySpider(CrawlSpider):
    name = 'Radio'
    allowed_domains = ['annuaireradio.fr']
    
    with open('gl.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', quotechar='"')
   

        liste = [str(i[1]) for i in spamreader if len(str(i[1]))  > 4 ]
    
    
    start_urls = [
        "http://www.annuaireradio.fr/commune.php?mode=searchville&insee=%s" % i for i in liste
    ]

    log.msg(liste, log.INFO)
    


    def parse(self, response):
        log.msg("Parse", level=log.INFO)
        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//table/tr') 

        

        for row in rows:
            
            Zone = response.url
            Frequence=row.select('.//td/span/text()').extract() 
            Radio=row.select('.//td/a[@href]/text()').extract(),
            Intensite=row.select('.//td/table/tr/td[2]').extract()

            yield ScrapyRadioItem(Zone=Zone,Frequence=Frequence,Radio=Radio,Intensite=Intensite)
