import requests
import bs4
import re



response = requests.get('https://wordsonline.ru/%D0%90')

html_page = bs4.BeautifulSoup(response.text, 'html.parser')

h1 = html_page.find('h1').text
print(h1)

print()

p_text = html_page.find('p').text
print(p_text)

print()

all_div = html_page.find_all('div', {'class': 'col-sm-3 col-xs-6'})

for div in all_div:

     all_li = div.find_next('ul').find_next('li').find_all_next('a')
     
     for a in all_li:

          href = 'https://wordsonline.ru' + a.get('href')
          
          if '/А/' in href:
               print(href)

               print(a.text)
