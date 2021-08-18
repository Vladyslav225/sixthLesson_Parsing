import requests
import bs4


data = []


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

     d = {}

     href = objs.get('href')

     if '/А/' in href:
          
          clean_href = 'https://wordsonline.ru' + href

          get_a = objs.get_text('a')

          d['a'] = get_a
          d['href'] = clean_href

          return d


url = 'https://wordsonline.ru/%D0%90'

url_obj = get_url(url)

get_objs = get_div_class(bs4_obj=url_obj)

for objs in get_objs:

     obj = get_clean_obj(objs)

     if obj == None:
          continue

     data.append(obj)

for n in data:
     print(n)

