import requests
from bs4 import BeautifulSoup

page = requests.get('URL')
soup = BeautifulSoup(page.txt, 'html.parser')

blockquote_items = soup.find_all('blockqoute')
for blockquote in blockquote_items:
    autor = blockquote.find(class_= 'author').text
    categoria = blockquote.find(class_='cat').text
    frase = blockquote.find('q').text

    print([autor, categoria, frase])
