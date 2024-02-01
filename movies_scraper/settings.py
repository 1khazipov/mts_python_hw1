BOT_NAME = "movies_scraper"

SPIDER_MODULES = ["movies_scraper.spiders"]
NEWSPIDER_MODULE = "movies_scraper.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEED_FORMAT = 'csv'
FEED_URI = 'movies_data.csv'
