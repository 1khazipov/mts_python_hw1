from scrapy.item import Item, Field


class MovieItem(Item):
    title = Field()
    genre = Field()
    director = Field()
    country = Field()
    year = Field()