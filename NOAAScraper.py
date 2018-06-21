# NOAA forecast scraper
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

data = []
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=44.98323860000005&lon=-93.27220729999999#.WtjBrC-ZPJw')
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_='tombstone-container')
period_tags = seven_day.select('.tombstone-container .period-name')
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select('.tombstone-container .short-desc')]
temps = [t.get_text() for t in seven_day.select('.tombstone-container .temp')]
descs = [d['title'] for d in seven_day.select('.tombstone-container img')]
period_tags = seven_day.select('.tombstone-container .period-name')

import pandas as pd
weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc": descs
 })

print(weather)
with open('index2.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for periods, short_descs, temps, descs in data:
        writer.writerow([periods, short_descs, temps, descs, datetime.now()])

# temp_nums = weather['temp'].str.extract("(?P<temp_num>d+)", expand=False)
# weather['temp_num'] = temp_nums.astype("int")
# print(temp_nums)



