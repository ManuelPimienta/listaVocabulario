import requests
from bs4 import BeautifulSoup

url = "https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


# sopa = BeautifulSoup("<li><a href=\"https://es.wiktionary.org/wiki/humano\" title=\"humano\">humano</a></li>")
listaPalabrasComunes = []
# results = soup.ul.li.a
for elements in soup:
    # results = soup.li.a
    print(soup.find_all('a')) 
for link in soup.find_all('a'):
    listaPalabrasComunes.append(link.get('title'))

with open("source\palabrasComunes.txt", "w") as f:
    for i in listaPalabrasComunes:
        f.write(i)
    
# f.close()
# f = open("source\palabrasComunes.txt", "w+")
# for i in palabrasComunes:
#         f.write(i)
f.close()

print(listaPalabrasComunes)