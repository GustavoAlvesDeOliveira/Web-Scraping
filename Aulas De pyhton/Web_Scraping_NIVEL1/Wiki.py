import requests
from lxml import html

encabecado = {
    "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
url = "https://www.wikipedia.org/"

resp = requests.get(url, headers=encabecado)

parser = html.fromstring(resp.text)

portuguesenumeros = parser.get_element_by_id("js-link-box-en")
portugues = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(portugues)

print(portuguesenumeros.text_content())



