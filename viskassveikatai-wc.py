from selenium import webdriver

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('viskassveikatai-wc.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Photo_url', 'Price', 'Link_to_page', 'Bigger_photo_url', 'Description']
outputWriter.writerow(column_names)

main_link = 'https://www.viskassveikatai.lt/slaugos-priemones-technika/vonios-tualeto-reikmenys?limit=100'

#open Chrome
driver = webdriver.Chrome()
driver.get(main_link)

#finding all product titles and links to the page of each product
titles = driver.find_elements_by_class_name('name')
title_strings = [title.text for title in titles]
attributes_in_titles = [title.find_element_by_tag_name('a') for title in titles]
links = [link.get_attribute('href') for link in attributes_in_titles]
print(title_strings)
print(links)

#finding all photos / thumbnail images
photo_urls = []
image_containers = driver.find_elements_by_class_name('image')
for container in image_containers:
    photo = container.find_element_by_tag_name('img')
    photo_url = photo.get_attribute('src')
    photo_urls.append(photo_url)
print('\n'.join(map(str, photo_urls)))

#finding all prices
prices = driver.find_elements_by_class_name('price')
price_strings = [price.text for price in prices]
print(price_strings)