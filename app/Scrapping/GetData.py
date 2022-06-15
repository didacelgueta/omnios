import requests
from bs4 import BeautifulSoup

from app.Actions.GetDescription import GetDescription

class GetData:
    def __init__(self, url) -> None:
        self.url = url
        self.base_url = 'http://books.toscrape.com/catalogue/'

    def __get_attributes(self, book: str) -> list:
        title = book.h3.a.get('title')
        rating = book.p.get('class')[1]
        price = book.select('p')[1].get_text(strip=True)
        description = GetDescription().handle(self.base_url + book.select('h3 > a')[0].get('href'))
        image_url = book.select('img')[0]['src']

        return [title, rating, price, description, image_url]


    def gather_data_from_webside(self, pages_amount: int = None):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')

        books = soup.find_all('article')

        books_info = [self.__get_attributes(books[0])]

        if pages_amount is None:
            pages_amount = int(soup.find_all("li", {"class": "current"})[0].get_text(strip=True).split(' ')[-1])

        for i in range(2, pages_amount+1):
            new_url = self.url.replace('1', str(i))
            url = new_url
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')

            books = soup.find_all('article')

            for index, book in enumerate(books):
                attributes = self.__get_attributes(book)
                books_info.append(attributes)

        return books_info
