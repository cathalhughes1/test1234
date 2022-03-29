import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://sipwhiskey.com/collections/japanese-whisky
#https://sipwhiskey.com/collections/japanese-whisky/products/nikka-coffey-malt-whisky

#https://www.yelu.uk/category/others
#https://www.yelu.uk/company/1187096/tenancy-cleaning-services
class QuotesSpider(CrawlSpider):
    name = "quotes"
    allowed_domains= ['europages.co.uk']
    start_urls = ['https://www.europages.co.uk/']

    rules = (
        Rule(LinkExtractor(allow='category', deny='company')),
        Rule(LinkExtractor(allow='company'),callback='parse_item')

    )

    def parse_item(self, response):
        yield {
            'brand' : response.xpath('//*[@id="company_name"]/text()').get()
        }