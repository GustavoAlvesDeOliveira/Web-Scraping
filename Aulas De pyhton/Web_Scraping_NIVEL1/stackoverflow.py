import requests
from bs4 import BeautifulSoup

encabecado = {
    "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Connection": "keep-alive"
}

url = "https://stackoverflow.com/questions"

resp = requests.get(url, headers=encabecado)

soup = BeautifulSoup(resp.text, "html.parser")

as_perguntas = soup.find_all('div', class_="s-post-summary")

for pergunta in as_perguntas:
    texto_pergunta = pergunta.find('h3').text
    print(texto_pergunta)

