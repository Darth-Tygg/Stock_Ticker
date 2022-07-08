# This is a simple single stock ticker that grabs the current stock price.

# Importing dependencies
import requests
import bs4
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *


# Creating a GUI Window
window = Tk()

# Getting the user to input desired stock ticker.
t1 = tk.Label(master=window, text='What is the stock ticker? ')
t1.pack()


# Create a function for the button to execute
def stock_ticker():
    name = entry.get()
    web_site = requests.get(f'https://www.google.com/finance/quote/{name}:NASDAQ')
    soup = bs4.BeautifulSoup(web_site.text, 'lxml')
    stock = soup.find('div', class_='YMlKec fxKbKc').text
    label_1 = Label(window, text=f"Current of {name} Price is {stock}")
    label_1.pack()


# Create a button
button_1 = Button(window, text="Click Here", padx=50, pady=5, relief=tk.RAISED, borderwidth=5, command=stock_ticker)
button_1.pack()

# Create a Frame, with a Relief
frame_a = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
frame_a.pack()

# Create an entry widget
entry = tk.Entry()
entry.pack()

# This tells Python to run the Tkinter event loop.
window.mainloop()
