import requests
from bs4 import BeautifulSoup


class GetDescription:
    @staticmethod
    def handle(url: str) -> str:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        return soup.find('article').select('p')[3].get_text(strip=True)
