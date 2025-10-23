#pip install requests
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = "http://books.toscrape.com"

response = requests.get(URL)

if response.status_code == 200:
    # data = response.content
    # print(data)
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    #print(books[0])
    rows = []
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p',class_='price_color').get_text()
        if 'rows' not in globals():
            rows = []
        rows.append([title, price])
        
    print(tabulate(rows, headers=['Title', 'Price'], tablefmt='grid'))
        
        
else:
    print(f'error codigo {response.status_code}')