import requests
import csv
from bs4 import BeautifulSoup

pages = ['http://www.goldenvalley-cadillac.com/CadillacSpecials']
data = []
for pg in pages:
    page = requests.get(pg)
    soup = BeautifulSoup(page.text, 'html.parser')
    content = soup.find(class_='deck')
    unit_titles = content.findAll(itemprop='description')
    unit_info = [pt.getText() for pt in unit_titles]
    unit_models = content.findAll(itemprop='name')
    payment = [pt.getText() for pt in unit_models]
    print(unit_info)


    
    #df = pd.DataFrame(unit_list, columns = ['Year', 'Brand', 'Model'])
    #df.to_csv('MorriesUsedInv.csv', mode='a', header=False)
