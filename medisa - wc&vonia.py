# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['medisa.lt']
    start_urls = ['http://medisa.lt/199-vonios-duso-iranga-ir-priemones?order=product.name.asc']

    def parse(self, response):
        self.log('I just visited' + response.url)
        yield {
            'title': response.xpath('//*[@id="js-product-list"]/div/article/div/div/h1/a').extract(),
            'link': response.xpath('//*[@id="js-product-list"]/div/article/div/div/h1/a/@href').extract(),
            'price': response.css('.price::text').extract(),
            'photo': response.xpath('//*[@id="js-product-list"]/div/article/div/a/img/@src').extract(),
            'bigger_photo': response.xpath(
                '//*[@id="js-product-list"]/div/article/div/a/img/@data-full-size-image-url').extract(),
        }
