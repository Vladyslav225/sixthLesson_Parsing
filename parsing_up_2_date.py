import requests
import bs4


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

     objects = {}

     
     get_href = items.a.get('href')

     get_a_text = items.get_text('a')

     objects['href'] = get_href
     objects['a'] = get_a_text

     return objects



url = 'https://up2date.com.ua/igrovie-pristavki/igry-ps4.html'

basic_url = get_basic_page(url)
# print(basic_url)

div_rows = basic_url.find('div', {'class': 'row grid-rows'})
# print(div_rows)

div_products = get_all_products(products=div_rows)
# print(div_products)
list_products.append(div_products)


for items in div_products:

     a_href = get_a_text_hrefs(items)

     print(a_href)









