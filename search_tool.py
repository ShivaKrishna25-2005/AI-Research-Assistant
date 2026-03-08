from ddgs import DDGS
import requests
from bs4 import BeautifulSoup


def search_articles(query):

    articles = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for r in results:
            url = r["href"]

            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")

                paragraphs = soup.find_all("p")
                text = " ".join([p.get_text() for p in paragraphs])

                articles.append(text)

            except:
                continue

    return articles