import requests
from bs4 import BeautifulSoup

#url of the air Jordan products

URL = "https://www.hollisterco.com/shop/ca/mens"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

div_product_name = soup.find_all('div',attrs={'class':'product-name'})
span_product_price = soup.find_all('span',attrs={'class':'product-price'})

for name, price in zip(div_product_name, span_product_price):
    product_name = name.find('h2')
    product_price = price.find('span')
    print("Product Name:", product_name.text)
    print("Product Price:", product_price.text)




