from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

url = 'https://www.daraz.com.bd/traditional-laptops/'

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()

all_products = []
products = driver.find_elements(By.CSS_SELECTOR, '.c5TXIP')


for product in products:
    links = product.find_elements(By.TAG_NAME, 'a')
    product_price = product.find_element(By.CLASS_NAME, 'c13VH6').text
    for link in links:
        product_name = link.get_attribute('title')
    product_info = {
        'name': product_name,
        'price': product_price
    }
    all_products.append(product_info)

# print(all_products)

if all_products:
    with open('laptops.csv', 'w', encoding='utf8', newline='') as file:
        write = csv.DictWriter(file, all_products[0].keys(),)
        write.writeheader()
        write.writerows(all_products)
        print('Scraped Successfully')
else:
    print('Failed to scrape')

# def get_products(link):
#     driver.get(link)
#     product_name = driver.find_element(
#         By.CLASS_NAME, 'pdp-mod-product-badge-title')
#     product_price = driver.find_element(By.CLASS_NAME, 'pdp-price')
#     return product_name, product_price


# for product in products:
#     links = product.find_elements(By.TAG_NAME, 'a')
#     for link in links:
#         product_link = link.get_attribute('href')
#         all_products.append(get_products(product_link))
#         time.sleep(5)
