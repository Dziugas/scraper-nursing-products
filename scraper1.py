from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('pirmaszingsnis-wc.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Photo_url', 'Price', 'Link_to_page']
outputWriter.writerow(column_names)

cycle_list = ['Title', 'Photo_url', 'Price', 'Link_to_page']

# a variable to generate IDs

link = 'https://www.pirmaszingsnis.lt/Produktai/slaugos-priemones/wc-ir-vonios-reikmenys'

driver = webdriver.Chrome()
driver.get(link)

titles = driver.find_elements_by_class_name('title-block')
title_strings = [title.text for title in titles]

photos = driver.find_elements_by_tag_name('img')
photo_urls = [photo.get_attribute('src') for photo in photos]

prices = driver.find_elements_by_class_name('price-block')
price_strings = [price.text for price in prices]

links = driver.find_elements_by_class_name('ext_button')
link_hrefs = [link.get_attribute('href') for link in links]

all = list(map(list, zip(title_strings, photo_urls, price_strings, link_hrefs)))
print(all)

id = 1
for row in list(all):
    row.insert(0, id)
    row.insert(1, link)
    outputWriter.writerow(row)
    id+=1

# close the .csv file
outputFile.close()

# close driver/browser
driver.close()

#fix the end time of running the script
end_time = time.clock()

#print the time it took to run the code
print(end_time-start_time)