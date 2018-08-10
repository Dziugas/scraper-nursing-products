# -*- coding: utf-8 -*-
import scrapy

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('medisa-wc&vonia.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Photo_url', 'Price', 'Link_to_page', 'Bigger_photo_url', 'Description']
outputWriter.writerow(column_names)


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['medisa.lt']
    start_urls = ['http://medisa.lt/199-vonios-duso-iranga-ir-priemones?order=product.name.asc']

    def parse(self, response):
        item = {
            'title': response.xpath('//*[@id="js-product-list"]/div/article/div/div/h1/a/text()').extract(),
            'link': response.xpath('//*[@id="js-product-list"]/div/article/div/div/h1/a/@href').extract(),
            'price': response.css('.price::text').extract(),
            'photo': response.xpath('//*[@id="js-product-list"]/div/article/div/a/img/@src').extract(),
            'bigger_photo': response.xpath(
                '//*[@id="js-product-list"]/div/article/div/a/img/@data-full-size-image-url').extract(),
        }
        yield item

        # follow pagination link
        next_page_url = response.css('.next::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        print(item)


        # loop through links
        # collect info


# write dictionary to the csv file


# close the .csv file
outputFile.close()

#fix the end time of running the script
end_time = time.clock()

#print the time it took to run the code
print(end_time-start_time)