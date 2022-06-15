import requests
from textblob import TextBlob


class AddData:
    def __init__(self, data: list) -> None:
        self.data = data

    def __add_random_name(self) -> list:
        url = "https://randommer.io/api/Name"
        token = '51b42309dfa84a5c9f2ca2c91bce4e2e'

        headers = {
        "accept" : "application/json",
        "X-Api-Key": str(token)
        }

        names = requests.get(url, headers=headers, params={'nameType': 'fullname', 'quantity': len(self.data)}).json()

        return names

    def __add_translations(self, book: str) -> list:
        blob = TextBlob(book[3])
        sp_description = blob.translate(from_lang='en', to='es')
        fr_description = blob.translate(from_lang='en', to='fr')

        return [sp_description, fr_description]

    def add_extra_fields(self) -> list:
        names = self.__add_random_name()
        extended_data = []
        for index, book in enumerate(self.data, start=1):
            if isinstance(book, list):
                translation = self.__add_translations(book)
                extended_data.append([
                    index,
                    names[index-1],
                    book[0],
                    book[1],
                    book[2],
                    book[4],
                    book[3],
                    str(translation[0]),
                    str(translation[1])
                ])

        return extended_data
