from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://denver.craigslist.org/search/sss?query=iphone+7&sort=rel'

page_html = requests.get(my_url)
page_soup = soup(page_html.content, "html.parser")

products = page_soup.findAll("li", {"class": "result-row"})

for product in products:
    time_created = product.find('time')['datetime']

    name_container = product.findAll("a", {"class": "result-title hdrlnk"})
    name_product = name_container[0].text

    links = product.find('a')['href']
    prefix = 'http://denver.craiglist.org'

    price = product.find('span', {'class': 'result-price'})
    time_created = product.find('time')['datetime']
    if price is None:
        pass
    else:
        price_product = price.text.strip()

    print("Time created: " + time_created)
    print("Name product: " + name_product)
    print("Price product: " + price_product)
    print("Links: " + prefix + links + '\n')
