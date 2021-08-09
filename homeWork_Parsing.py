import requests
import bs4


# /home/vladyslav/IT_Step/sixthLesson_Parsing/data/


response = requests.get('https://wordsonline.ru/')

html_page = bs4.BeautifulSoup(response.text, 'html.parser')

list_basic_links = []

div = html_page.find('div', class_= 'alphabet')

all_a = div.find_all('a')

for a in all_a:

     href = a.get('href')
     # print(href)

     # all_a = a.get_text('a')
     # print(all_a)

     # title = a.get('title')
     # # print(title)

     full_basic_links = ('https://wordsonline.ru' + href)
     # print(full_basic_links)
     list_basic_links.append(full_basic_links)

# print(list_basic_links)

for full_basic_links in list_basic_links:
     response = requests.get(full_basic_links)
     # print(response)

     html_page = bs4.BeautifulSoup(response.text, 'html.parser')
     # print(html_page)

     name_data = full_basic_links.split('/')[-1]
     print(name_data)

     all_data = html_page.find_all('div', class_ = 'col-sm-3 col-xs-6')
     print(all_data)
     

     # with open(f'{name_data}.html' 'w') as file:
     #      file.write


          
