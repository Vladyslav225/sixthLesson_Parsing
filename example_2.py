import requests
import bs4

response = requests.get('https://4pda.to/')

html_page = bs4.BeautifulSoup(response.text, "html.parser")
all_a = html_page.find_all("a")
list_clean_href = []
data = []


for a in all_a:

    href = a.get('href')
    if "https://" in href and href not in list_clean_href:
        obj = {}

        title = a.get('title')

        list_clean_href.append(href)
        obj['title'] = title
        obj['href'] = href
        data.append(obj)


for obj in data[:20]:
    title = obj['title']
    if not title:
        continue

    href = obj['href']
    response = requests.get(href)
    html_page_article = bs4.BeautifulSoup(response.text, "html.parser")
    text = html_page_article.find_all('p')

    obj['text'] = text[0]

for i in data:
    print(i)