import requests
import bs4
import re

from requests.api import delete


list_obj = []
list_ = []


def get_url(url):

     try:
          response = requests.get(url)

     except Exception as ex:
          print(ex)

     return bs4.BeautifulSoup(response.text, 'html.parser')


def get_div_class(bs4_obj):

     try:
          get_div = bs4_obj.find_all('div', {'class': 'col-sm-3 col-xs-6'})

     except:
          print("I can't find these attributes, check their presence in site design")
     
     for div in get_div:

          try:
               get_a = div.find_next('ul').find_next('li').find_all_next('a')

          except:
               print("I can't find these attributes, check their presence in site design")

          return get_a


def get_clean_obj(objs):

     # list_clean_href = []

     # print(objs)

     href = objs.get('href')

     if '/А/' in href:
          
          # list_clean_href.append(clean_heref)

          clean_href = 'https://wordsonline.ru' + href

          get_a = objs.get_text('a')

          return [get_a, clean_href]


url = 'https://wordsonline.ru/%D0%90'

url_obj = get_url(url)

get_objs = get_div_class(bs4_obj=url_obj)
# print(get_objs)

for objs in get_objs:

     obj = get_clean_obj(objs)

     if obj == None:
          continue
     print(obj)

