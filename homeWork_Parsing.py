import requests
import bs4


response = requests.get('https://wordsonline.ru/')

html_page = bs4.BeautifulSoup(response.text, 'html.parser')
# print(html_page)

list_links = []

all_div = html_page.find('div', class_= 'alphabet')
#print(all_div)

all_a = all_div.find_all('a')
# print(all_a)

for a in all_a:

     list_a = a.get_text('a')
     print(list_a)

     href = a.get('href')
     # print(href)
     if "http://wordsonline.ru" not in href:
          href = ('https://wordsonline.ru' + href)
          # href = full_link
          print(href)

     # list_links.append(href)

     title = a.get('title')
     print(title)

     



          
     


          
