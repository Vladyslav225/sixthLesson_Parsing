import requests
import bs4
import re


data = []

obj = {}

# try:

#      response = requests.get('https://wordsonline.ru')

# except Exception as ex:
#      print(ex)

# html_page = bs4.BeautifulSoup(response.text, 'html.parser')

# all_p = html_page.find_all('p')

# for p in all_p:

#      p_text = str(p.text)

#      try:
#           pattern = r'\w+'
#           n = re.findall(pattern, p_text)
#           print(n)

#      except:
#           print("I don't understend this text")

try:
     response = requests.get('https://wordsonline.ru/%D0%90')

except Exception as ex:
     print(ex)

html_page = bs4.BeautifulSoup(response.text, 'html.parser')

h1_text = html_page.find('h1').text

p_text = html_page.find('p').text

obj['h1'] = h1_text
obj['p'] = p_text

data.append(obj)

try:
     all_div = html_page.find_all('div', {'class': 'col-sm-3 col-xs-6'})

except:
     print("There is no tag with such a class")

for div in all_div:

     try:
          all_a = div.find_next('ul').find_next('li').find_all_next('a')
     
     except:
          print("I can't find these attributes, check their presence in site design")
     
     for a in all_a:

          try:
               href = 'https://wordsonline.ru' + a.get('href')

          except:
               print("Check the correct spelling of the links")
          
          if '/А/' in href:

               a_text = a.get_text('a')
               print(type(a_text))

               data.append(a_text)
               data.append(href)


# for n in data:
#      print(n)
