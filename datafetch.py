# coding: utf8
from bs4 import BeautifulSoup
import requests


url = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari"

def vericek(e):
    text = [""]
    data = [1, 2, 3, 4]
    r = requests.get(url)
    if str(r.status_code) != "200":
        return 0
    else:
        if e == "":
            text = "Tekrar deneyin."
            return 1
        else:
            soup = BeautifulSoup(r.text, "html.parser")
            fuel = soup.find('tr', {'data-disctrict-id': e})
            iladi = fuel["data-disctrict-name"]
            text = [iladi]
            fuelprice = fuel.find_all('span', {'class': 'with-tax'})
            data[0] = fuelprice[0].text
            data[1] = fuelprice[1].text
            data[2] = fuelprice[2].text
            data[3] = fuelprice[3].text
            textvedata = text + data
            return textvedata
        
    
    
    