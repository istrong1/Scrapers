import requests
import csv
from bs4 import BeautifulSoup

pages = ['http://www.goldenvalley-cadillac.com/VehicleSearchResults?search=preowned%2Ccertified','http://www.goldenvalley-cadillac.com/VehicleSearchResults?search=preowned%2Ccertified&limit=24&offset=24','http://www.goldenvalley-cadillac.com/VehicleSearchResults?search=preowned%2Ccertified&limit=24&offset=48', 'http://www.goldenvalley-cadillac.com/VehicleSearchResults?search=preowned%2Ccertified&limit=24&offset=72', 'http://www.goldenvalley-cadillac.com/VehicleSearchResults?search=preowned%2Ccertified&limit=24&offset=96']
data = []
for pg in pages:
    page = requests.get(pg)
    soup = BeautifulSoup(page.text, 'html.parser')
    content = soup.find(class_='deck')
    unit_model_years = content.findAll(itemprop='vehicleModelDate')
    model_year = [pt.getText() for pt in unit_model_years]
    unit_brands = content.findAll(itemprop='manufacturer')
    brands = [pt.getText() for pt in unit_brands]
    unit_model = content.findAll(itemprop='model')
    model = [pt.getText() for pt in unit_model]

    import pandas as pd
    unit_list = pd.DataFrame({
    'Year': model_year,
    'Brand': brands,
    'Model': model
    })

    df = pd.DataFrame(unit_list, columns = ['Year', 'Brand', 'Model'])
    df.to_csv('MorriesUsedInv.csv', mode='a', header=False)
