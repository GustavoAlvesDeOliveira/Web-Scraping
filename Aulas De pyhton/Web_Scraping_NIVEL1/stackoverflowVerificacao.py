import requests
from bs4 import BeautifulSoup

encabecado = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Connection": "keep-alive"
}

url = "https://stackoverflow.com/questions"

resp = requests.get(url, headers=encabecado)

print(resp.status_code)  # verificar se carregou

soup = BeautifulSoup(resp.text, "html.parser")

as_perguntas = soup.select(".s-post-summary h3")

print(len(as_perguntas))  # ver quantas encontrou

for pergunta in as_perguntas:
    titulo = pergunta.find('h3')
    
    if titulo:
        print(titulo.get_text(strip=True))