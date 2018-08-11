# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['medisa.lt']
    start_urls = ['http://medisa.lt/199-vonios-duso-iranga-ir-priemones?order=product.name.asc']

    def parse(self, response):
        for product in response.css('.thumbnail-container'):
            item = {
                'title': product.css('h1.product-title a::text').extract(),
                'link': product.css('h1.product-title a::attr(href)').extract(),
                'price': product.css('span.price::text').extract(),
                'photo': product.css('img::attr(src)').extract(),
                'bigger_photo': product.css('img::attr(data-full-size-image-url)').extract(),
            }
            yield item

        urls = response.css('h1.product-title a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_details)

        # follow the pagination link
        next_page_url = response.css('a.next::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        yield {
            'description': response.css('div.product-description span::text').extract()
        }

        # todo: join dictionaries, write to csv/json, count execution time, clean the results...
