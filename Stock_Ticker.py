# This is a simple single stock ticker that grabs the current stock price.

# Importing dependencies
import requests
import bs4
from bs4 import BeautifulSoup

# Getting the user to input desired stock ticker.
t1 = input('What is the ticker? ')


# Creating the function
def stock_ticker():
    web_site = requests.get(f'https://www.google.com/finance/quote/{t1}:NASDAQ')
    soup = bs4.BeautifulSoup(web_site.text, 'lxml')
    stock = soup.find('div', class_='YMlKec fxKbKc').text
    return stock


print(stock_ticker())
