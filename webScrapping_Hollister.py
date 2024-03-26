# importing required libraries 
import requests
from bs4 import BeautifulSoup

# Targets the URL for the specific website
URL = "https://www.hollisterco.com/shop/ca/mens"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

# Access the div tag with the product name
div_product_name = soup.find_all('div',attrs={'class':'product-name'})

# Access the span tag with the product price
span_product_price = soup.find_all('span',attrs={'class':'product-price'})

# Loop to find and print all the products names and price 
for name, price in zip(div_product_name, span_product_price):
    product_name = name.find('h2')
    product_price = price.find('span')
    print("Product Name:", product_name.text)
    print("Product Price:", product_price.text)




