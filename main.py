import pandas as pd
from app.Scrapping.GetData import GetData
from app.Scrapping.AddData import AddData

# Gather books data from website
books = GetData('http://books.toscrape.com/catalogue/page-1.html').gather_data_from_webside(pages_amount=5)

# Add extra info
books_info = AddData(books).add_extra_fields()

# Save output to csv
df = pd.DataFrame(books_info, columns=['id', 'name', 'title', 'rating', 'price', 'image_url', 'desc_en', 'desc_es', 'desc_fr'])
df.set_index('id', inplace=True)
df.to_csv('books_info.csv')
