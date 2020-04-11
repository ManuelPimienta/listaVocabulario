from bs4 import BeautifulSoup
from collections import Counter
import requests

lista_paginas = 'http://sostenibilidad.semana.com/medio-ambiente/articulo/ciudad-del-cabo-sin-agua-once-ciudades-mas-que-pueden-sufrir-lo-mismo/39459'
lista = []
lista2 = []
lista3 = []
lista4 = []
lista_sustantivos = ['time', 'issue', 'year', 'side', 'people', 'kind', 'way', 'head', 'day', 'house', 'man', 'service', 'thing', 'friend', 'woman', 'father', 'life', 'power', 'child', 'hour', 'world', 'game', 'school', 'line', 'state', 'end', 'family', 'member', 'student', 'law', 'group', 'car', 'country', 'city', 'problem', 'community', 'hand', 'name', 'part', 'president', 'place', 'team', 'case', 'minute', 'week', 'idea', 'company', 'kid', 'system', 'body', 'adsbygooglewindowadsbygoogle', '||', 'push', 'remove', 'ads', 'program', 'information', 'question', 'back', 'work', 'parent', 'government', 'face', 'number', 'others', 'night', 'level', 'mr', 'office', 'point', 'door', 'home', 'health', 'water', 'person', 'room', 'art', 'mother', 'war', 'area', 'history', 'money', 'party', 'story', 'result', 'fact', 'change', 'month', 'morning', 'lot', 'reason', 'right', 'research', 'study', 'girl', 'book', 'guy', 'eye', 'food', 'job', 'moment', 'word', 'air', 'business', 'teacher']
clean_word_list = []

lista_final = []
# pagina in lista_paginas:
leer_pag = requests.get(lista_paginas)
contenido = leer_pag.content
soup = BeautifulSoup(contenido, 'html.parser')
texto = soup.find_all('p')
# Agregar palabras a la lista.
for pal in soup.find_all('p'):
    lista.append(pal.get_text().split())

for palabra in lista:
    lista2.append(palabra)

for x in lista2:
    for y in x:
        lista3.append(y)

for word in lista3:
    symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='0123456789"
    for i in range(0, len(symbols)):
        word = word.replace(symbols[i], "")
    if len(word) > 0:
        clean_word_list.append(word)

for w in clean_word_list:
    letras = w.lower()
    if len(letras) > 3:
        lista4.append(letras)

for pala in lista4:
    if pala in lista_sustantivos:
        pass
    else:
        lista_final.append(pala)
print(clean_word_list)
cuenta_palabras = Counter(lista_final)
top = cuenta_palabras.most_common(20)
print(top)
