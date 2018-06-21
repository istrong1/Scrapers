# website scraper for the S&P mini futures and Dow J mini futures
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

data = []
myurl = ['https://www.bloomberg.com/quote/ES1:IND', 'https://www.bloomberg.com/quote/DM1:IND', 'https://www.bloomberg.com/quote/GBTC:US']
for pg in myurl:
    html = requests.get(pg).content
    soup = BeautifulSoup(html, "html.parser")
    name_box = soup.find('h1', attrs={'class': 'name'})
    name = name_box.text.strip()
    print (name)

    price_box = soup.find('div', attrs={'class': 'price'})
    price = price_box.text
    print (price)
    
    ticker_box = soup.find('div', attrs={'class': 'ticker'})
    ticker = ticker_box.text.strip()
    data.append((name, price, ticker))
#open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price, ticker in data:
        writer.writerow( [name, price, ticker, datetime.now()])