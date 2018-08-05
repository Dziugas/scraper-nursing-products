import bs4
import requests

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('slaugosiranga-wc.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Photo_url', 'Price', 'Link_to_page', 'Bigger_photo_url', 'Description']
outputWriter.writerow(column_names)

main_link = 'http://slaugosiranga.lt/produkto-kategorija/vonia-ir-tualetas/'

res = requests.get(main_link)
wc = bs4.BeautifulSoup(res.text)


titles_raw = wc.select('.woocommerce-loop-product__title')
titles = [title.getText() for title in titles_raw]

prices_raw = wc.select('.price')
prices = [price.getText() for price in prices_raw]

links_raw = wc.select('.woocommerce-LoopProduct-link')
links = [link.get('href') for link in links_raw]

photos_raw = wc.select('.attachment-shop_catalog')
photos = [photo.get('src') for photo in photos_raw]

descriptions = []
big_photos = []
for link in links:
    response = requests.get(link)
    product_info = bs4.BeautifulSoup(response.text)

    #bigger photos
    #todo: option to select more photos (with a limit)
    photos_list = product_info.select('.attachment-shop_single')
    photo_element = photos_list[0].get('src')
    big_photos.append(photo_element)

    #descriptions
    #todo: remove first paragraph if possible ('Aprasymas')
    description_list = product_info.select('.woocommerce-Tabs-panel')
    description_element = description_list[0].text
    descriptions.append(description_element)

all = list(map(list, zip(titles, photos, prices, links, big_photos, descriptions)))
print(all)

id = 1
for row in all:
    row.insert(0, id)
    row.insert(1, main_link)
    outputWriter.writerow(row)
    id+=1

# close the .csv file
outputFile.close()

#fix the end time of running the script
end_time = time.clock()

#print the time it took to run the code
print(end_time-start_time)