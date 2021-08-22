import requests
import bs4


list_href_products = []
list_products = []


def get_basic_page(url):

     try:
          req = requests.get(url)

     except Exception as ex:
          print(ex)

     return bs4.BeautifulSoup(req.text, 'html.parser')


def get_all_products(products):

     try:
          get_products = products.find_all('div', {'class': 'product-thumb minicard minicard--catalog'})

     except Exception as ex:
          print(ex)

     return get_products


def get_a_text_hrefs(items):

     # objects = {}

     try:
          get_href = items.a.get('href')

     except Exception as ex:
          print(ex)

          # get_a_text = items.get_text('a')

          # objects['href'] = get_href
          # objects['a'] = get_a_text

     return get_href

#################

def get_data_collection(data):

     try:
          req_data = requests.get(data)

     except Exception as ex:
          print(ex)

     return bs4.BeautifulSoup(req_data.text, 'html.parser')


def get_data_products(data_products):

     prod_name = data_products.find('h1', {'id': 'prod_name'}).text

     prod_price = data_products.find('div', {'class': 'product-page-price'}).text
     
     prod_text = data_products.find('div', {'id': 'tab-description'}).text

     list_products.append(f'Название игры: {prod_name}')
     list_products.append(f'Цена за игру: {prod_price}')
     list_products.append(prod_text)
   
     return list_products



url = 'https://up2date.com.ua/igrovie-pristavki/igry-ps4.html'

basic_url = get_basic_page(url)

div_rows = basic_url.find('div', {'class': 'row grid-rows'})

div_products = get_all_products(products=div_rows)


for items in div_products:

     a_href = get_a_text_hrefs(items)

     list_href_products.append(a_href)

for data in list_href_products:

     data_collection = get_data_collection(data)

     products_name = get_data_products(data_products=data_collection)

for prod in list_products:

     print(prod)
     print("----------------------------")

with open('file_parsing.txt', 'w') as file:
     for prod in list_products:
          file.write(prod)
          file.close
          



