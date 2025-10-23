import requests
from bs4 import BeautifulSoup
import json

URL = "https://neoauto.com/venta-de-autos-usados"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL,headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    autos = soup.find_all("article", class_="c-results c-results-used--premium")
    
    for art in autos:
        data = json.loads(art["data-gtm"])
        title = art.find("h2", class_="c-results__header-title").text.strip()
        link = art.find("a", class_="c-results__link")["href"]
        tag = art.find("div", class_="c-results-tag__stick")
        if tag:
            tag = tag.get_text()
        image = art.find("img", class_="c-results-slider__img-inside")["data-src"]
        fuel = art.find("span", class_="c-results-used__detail-fuel").text.strip()
        location = art.find("span", class_="c-results-details__description-text--highlighted").text.strip()
        price = art.find("div", class_="c-results-mount__price").text.strip()

        print({
            "titulo": title,
            "link": link,
            "etiqueta": tag,
            "imagen": image,
            "combustible": fuel,
            "ubicacion": location,
            "precio": price,
            "marca": data["item_brand"],
            "año": data["item_year"],
            "anunciante": data["item_advertiser"]
        })
else:
    print(f'error codigo {response.status_code} {response.reason}')