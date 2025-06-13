import requests
from bs4 import BeautifulSoup
from src.utils.helpers import get_output_paths, save_raw

def scrape_books(base_url, **kwargs):

    url = base_url + "catalogue/page-1.html"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    books = []
    for tag in soup.select("article.product_pod"):
        title = tag.h3.a["title"]
        price = tag.select_one(".price_color").text.strip()
        books.append({"title": title, "price": price})
    paths = get_output_paths()
    save_raw(books, paths["raw"])
    return books
