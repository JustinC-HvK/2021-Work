import requests
import bs4 
from bs4 import BeautifulSoup

global name
global address
global phone
namelist = []

def scape_work(url):

    pages = ['', -1, -2, -3, -4, -5]
    indexs = ['computers']
    
    for cat in indexs:
        for page in pages:
            pagehtml = requests.get(f"https://www.nzdirectory.co.nz/{cat}{page}.html")

            soup1=BeautifulSoup(pagehtml.text, 'html.parser')
            for info in soup1.find_all('div',class_="listing_content"):
                details=info.find(class_="address")

                try:
                    if details is not None:
                        i, phone = details.text.split('+', 1)
                        name, address = i.split(',',1)
                        namelist.append([name,address,phone])

                except:
                    pass
        return namelist


scape_work("https://www.nzdirectory.co.nz/index.html")

