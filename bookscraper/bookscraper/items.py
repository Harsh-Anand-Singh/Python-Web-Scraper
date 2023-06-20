import scrapy


class BookscraperItem(scrapy.Item):
    # defined the fields for the item here like:
    name = scrapy.Field()
    pass


def serialize_price(value):
    return f'£ {str(value)}'


class BookItem(scrapy.Item):
   url = scrapy.Field()
   title = scrapy.Field()
   upc = scrapy.Field()
   product_type = scrapy.Field()
   price_excl_tax = scrapy.Field()
   price_incl_tax = scrapy.Field()
   tax = scrapy.Field()
   availability = scrapy.Field()
   num_reviews = scrapy.Field()
   stars = scrapy.Field()
   category = scrapy.Field()
   description = scrapy.Field()
   price = scrapy.Field()
