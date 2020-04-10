from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "html.parser")

print(soup.prettify)