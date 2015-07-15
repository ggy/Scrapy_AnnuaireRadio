# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrapyRadioItem(Item):
    # define the fields for your item here like:
    Zone = Field()
    Frequence = Field()
    Radio = Field()
    Intensite = Field()

class BigCityItem(Item):
    City = Field()
