# coding: utf8
from bs4 import BeautifulSoup
import requests


url = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari"

class dataFetch:
    hatakodu = None
    iladi = None
    vmaxKursunsuz = 1
    vmaxDiesel = 2
    vpro = 3
    pogaz = 4
            
        
def getFuelPriceData(e):
    dataFetchClass = dataFetch()
    r = requests.get(url)
    if str(r.status_code) != "200":
        dataFetchClass.hatakodu = 0
        return dataFetchClass
    
    if e == "":
        dataFetchClass.hatakodu = 1
        return dataFetchClass
        
    soup = BeautifulSoup(r.text, "html.parser")
    fuel = soup.find('tr', {'data-disctrict-id': e})
    dataFetchClass.iladi = fuel["data-disctrict-name"]
    fuelprice = fuel.find_all('span', {'class': 'with-tax'})
    dataFetchClass.vmaxKursunsuz = fuelprice[0].text
    dataFetchClass.vmaxDiesel = fuelprice[1].text
    dataFetchClass.vpro = fuelprice[2].text
    dataFetchClass.pogaz = fuelprice[3].text
    return dataFetchClass
        
    
    
    