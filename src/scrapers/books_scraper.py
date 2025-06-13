import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_books(base_url: str, output_path: str):
    books = []
    page = 1
    while True:
        url = f"{base_url}catalogue/page-{page}.html"
        r = requests.get(url)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.text, 'html.parser')
        for item in soup.select('.product_pod'):
            title = item.h3.a['title']
            price = item.select_one('.price_color').text
            stock = item.select_one('.availability').text.strip()
            rating = item.p['class'][1]
            category = soup.select_one('ul.breadcrumb li:nth-child(3) a').text
            books.append({
                'title': title,
                'price': price,
                'stock': stock,
                'rating': rating,
                'category': category,
            })
        page += 1
    df = pd.DataFrame(books)
    df.to_csv(output_path, index=False)
