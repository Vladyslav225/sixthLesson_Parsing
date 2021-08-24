import requests
import bs4
import json
import csv
import re



list_basic_data = []

list_parsing_basic_data = []


def get_basic_page(url):

     try:
          req = requests.get(url)

     except Exception as ex:
          print(ex)

     return bs4.BeautifulSoup(req.text, 'html.parser')

def get_a_href(basic_a_href):

     obj = {}

     try:
          get_href = basic_a_href.a.get('href')

     except Exception as ex:
          print(ex)

     try:
          get_a_txt = basic_a_href.a.img.get('title')

     except Exception as ex:
          print(ex)

     obj['Нaзвание игры: '] = get_a_txt
     obj['Ссылка к иге: '] = get_href

     return obj

def get_pars_data(pars_data):

     try:
          req = requests.get(pars_data['Ссылка к иге: '])

     except Exception as ex:
          print(ex)

     return bs4.BeautifulSoup(req.text, 'html.parser')

def get_title_price_description(h1_p_div, prod):

     try:
          product_title = h1_p_div.find('h1', {'id': 'prod_name'}).get_text().strip()

     except Exception as ex:
          print(ex)

     replace_list = product_title.replace(u'\xa0', u' ')

     try:
          product_price = h1_p_div.find('div', {'class': 'product-page-price'}).get_text().strip()

     except Exception as ex:
          print(ex)

     try:
          product_text = h1_p_div.find('div', {'id': 'tab-description'}).get_text().strip()

     except Exception as ex:
          print(ex)

     prod = [
          ['Название игры:', product_title],
          ['Цена за игру:', product_price],
          ['Описание:', product_text]
     ]

     return prod


url = 'https://up2date.com.ua/igrovie-pristavki/igry-ps4.html'

basic_url = get_basic_page(url)

div_row_products = basic_url.find('div', {'class': 'row grid-rows'}).find_all('div', {'class': 'product-thumb minicard minicard--catalog'})


for basic_a_href in div_row_products:

     a_href = get_a_href(basic_a_href)

     list_basic_data.append(a_href)

for pars_data in list_basic_data:

     all_data = get_pars_data(pars_data)

     title_price_description = get_title_price_description(h1_p_div=all_data, prod=pars_data)
     
     list_parsing_basic_data.append(title_price_description)

     with open('file_parsing.csv', 'w', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerows(list_parsing_basic_data)

     with open('file_parsing.json', 'w') as file:
          file.write(json.dumps(list_parsing_basic_data))
          file.close()

