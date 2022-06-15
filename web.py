from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('books_info.csv')

@app.route("/books")
def get_books():
    books = df.values.tolist()
    return jsonify(books)

@app.route("/book/<id>")
def get_book(id: str):
    book_info = df.loc[df['id'] == int(id)].values.tolist()
    return jsonify(book_info)

if __name__ == "__main__":
    app.run()
