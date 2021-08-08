import requests
import bs4
# from selenium import webdriver
# import time



# driver = webdriver.Firefox(executable_path='/home/vladyslav/IT_Step/sixthLesson_Parsing/geckodriver')

response = requests.get('https://wordsonline.ru/')

html_page = bs4.BeautifulSoup(response.text, 'html.parser')

list_links = []

all_div = html_page.find('div', class_= 'alphabet')

all_a = all_div.find_all('a')


try:
     # driver.get(url=response)
     # time.sleep(5)

     for a in all_a:

          list_a = a.get_text('a')
          # print(list_a)

          href = a.get('href')
          # print(href)

          if "http://wordsonline.ru" not in href:
               href = ('https://wordsonline.ru' + href)
               list_links.append(href)
               # print(list_links)

          title = a.get('title')
          # print(title)

     # for href in list_links:

     response = requests.get(list_links[0])
     html_page = bs4.BeautifulSoup(response.text, 'html.parser')
     print(html_page)

     # all_div = html_page.find('div', class_= 'alphabet')

except Exception as ex:
     print(ex)

# finally:
     # driver.close
     # driver.quit

          
     


          
