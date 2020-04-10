import requests
from bs4 import BeautifulSoup

url = "https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# sopa = BeautifulSoup("<li><a href=\"https://es.wiktionary.org/wiki/humano\" title=\"humano\">humano</a></li>")
palabrasComunes = []
# results = soup.ul.li.a
# for elements in soup:
#     # results = soup.li.a
#     print(soup.find_all('a')) 
for link in soup.find_all('a'):
    palabrasComunes.append(link.get('title'))

print(palabrasComunes)