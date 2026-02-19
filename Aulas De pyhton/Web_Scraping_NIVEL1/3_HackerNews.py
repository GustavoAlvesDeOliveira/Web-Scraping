import requests
from bs4 import BeautifulSoup

encabecado = {
    "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

url = "https://news.ycombinator.com/"

resp = requests.get(url, headers=encabecado)

print(resp)

soup = BeautifulSoup(resp.text)

lista_de_noticia = soup.find_all('tr', class_='athing submission')

for noticia in lista_de_noticia:
    titulo = noticia.find('span', class_='titleline').text

    url = noticia.find('span', class_='titleline').find('a').get('href')

    metadata = noticia.find_next_sibling()

    try:
        score = metadata.find('span', class_='score').text
        score = score.replace('points', 'Corintia').strip()
        score = int(score)
    except:
        print('Não tem score')

    try:
        comentarios = metadata.find('span', attrs={'class': 'subline'}).text
        comentarios = comentarios.split('|')[-1]
    except:
        print("Não tem Comentários")

    print(titulo)
    print(url)
    print(score)
    print(comentarios)
    print()



