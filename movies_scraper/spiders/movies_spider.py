import scrapy
from movies_scraper.items import MovieItem
from scrapy.selector import Selector
import re


class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/Категория:Фильмы_по_алфавиту"]

    def parse(self, response):
        for href in response.css("div.mw-category-group > ul > li > a::attr(href)"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_movie)

    def parse_movie(self, response):
        item = MovieItem()
        item['title'] = response.css('tr > th.infobox-above::text').get()
        clean_text = lambda text: ' '.join(text.split())
        item['genre'] = [clean_text(genre) for genre in response.xpath("//span[@data-wikidata-property-id='P136']//text()").extract() if clean_text(genre)]
        item['country'] = [clean_text(country) for country in response.xpath("//span[@data-wikidata-property-id='P495']//text()").extract() if clean_text(country)]
        item["year"] = clean_text(response.xpath("//span[@class='dtstart']/text()").get())
        if item['title'] or item['genre'] or item['country'] or item['year']:
            yield item
