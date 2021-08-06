import requests
import bs4
from selenium import webdriver


response = requests.get('https://wordsonline.ru/')

html_page = bs4.BeautifulSoup(response.text, 'html.parser')
# print(html_page)

# list_href = []
# data = []

all_div = html_page.find('div', class_= 'alphabet')
#print(all_div)

all_a = all_div.find_all('a')
# print(all_a)

for a in all_a:

     # obj = {}

     list_a = a.get_text('a')
     print(list_a)

     href = a.get('href')
     print(href)

     full_link = ('https://wordsonline.ru' + href)
     href = full_link
     print(href)

     title = a.get_text('title')
     print(title)



          
     


          
