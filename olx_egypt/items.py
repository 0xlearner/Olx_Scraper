# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxEgyptItem(scrapy.Item):
    URL = scrapy.Field()
    Breadcrumb = scrapy.Field()
    Price = scrapy.Field()
    Title = scrapy.Field()
    Type = scrapy.Field()
    Bedrooms = scrapy.Field()
    Bathrooms = scrapy.Field()
    Area = scrapy.Field()
    Location = scrapy.Field()
    keyword = scrapy.Field()
    Compound = scrapy.Field()
    seller = scrapy.Field()
    Seller_member_since = scrapy.Field()
    Seller_phone_number = scrapy.Field()
    Description = scrapy.Field()
    Amenities = scrapy.Field()
    Reference = scrapy.Field()
    Listed_date = scrapy.Field()
    Level = scrapy.Field()
    Payment_option = scrapy.Field()
    Delivery_term = scrapy.Field()
    Furnished = scrapy.Field()
    Delivery_date = scrapy.Field()
    Down_payment = scrapy.Field()
    Image_url = scrapy.Field()
