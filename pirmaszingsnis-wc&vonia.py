from selenium import webdriver

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('pirmaszingsnis-wc&vonia.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Photo_url', 'Price', 'Link_to_page', 'Bigger_photo_url', 'Description']
outputWriter.writerow(column_names)

main_link = 'https://www.pirmaszingsnis.lt/Produktai/slaugos-priemones/wc-ir-vonios-reikmenys'
#todo: fix comments
driver = webdriver.Chrome()
driver.get(main_link)

titles = driver.find_elements_by_class_name('title-block')
title_strings = [title.text for title in titles]

container = driver.find_element_by_xpath('//*[@id="page"]/div[3]/div/div[2]/div[2]/div[1]')
photos = container.find_elements_by_tag_name('img')
photo_urls = [photo.get_attribute('src') for photo in photos]


prices = driver.find_elements_by_class_name('price-block')
price_strings = [price.text for price in prices]

links = driver.find_elements_by_class_name('ext_button')
link_hrefs = [link.get_attribute('href') for link in links]
del link_hrefs[-4 : ]

bigger_photos = []
descriptions = []

for link in link_hrefs:
    driver.get(link)
    bigger_photo = driver.find_element_by_xpath('// *[ @ id = "page"] / div[3] / div / div[2] / div[2] / div[1] / div[2] / div / a / img')
    bigger_photo_url = bigger_photo.get_attribute('src')
    bigger_photos.append(bigger_photo_url)
    description_container = driver.find_element_by_class_name('product-cont')
    description_paragraphs = description_container.find_elements_by_tag_name('p')
    description_para_text = [paragraph.text for paragraph in description_paragraphs]
    description = ''
    for paragraph in description_para_text:
        description = description + ' ' + paragraph
    descriptions.append(description)

all = list(map(list, zip(title_strings, photo_urls, price_strings, link_hrefs, bigger_photos, descriptions)))
print(all)

# a variable to generate IDs
id = 1
for row in all:
    row.insert(0, id)
    row.insert(1, main_link)
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