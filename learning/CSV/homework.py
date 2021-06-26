# https://quotes.toscrape.com/
import csv

import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
html_data = BeautifulSoup(response.text, features='html.parser')
quotes = html_data.find_all(class_="quote")

with open('homework.csv', 'w') as file:
    headers = ['Quote', 'Author', 'Tags']
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow({
            'Quote': quote.find(class_='text').get_text(),
            'Author': quote.find(class_='author').get_text(),
            'Tags': quote.find(class_='keywords')['content']
        })


