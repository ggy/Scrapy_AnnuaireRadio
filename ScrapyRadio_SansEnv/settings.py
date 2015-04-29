# Scrapy settings for ScrapyRadio_SansEnv project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ScrapyRadio_SansEnv'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ScrapyRadio_SansEnv.spiders']
NEWSPIDER_MODULE = 'ScrapyRadio_SansEnv.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

LOG_LEVEL = 'DEBUG'
