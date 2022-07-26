
import requests
from bs4 import BeautifulSoup
from flask import Flask, request
import json

app = Flask(__name__)

def fetch_data():

    URL = "https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4"
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
                           
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    items = soup.find_all("div", {"class": "a-section a-spacing-small s-padding-left-small s-padding-right-small"})
    
    item_list = []
    for item in items:
        try:
            #print(item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text)
            #print(item.find("span", {"class": "a-price-whole"}).text + item.find("span", {"class": "a-price-fraction"}).text)
            name = item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
            
            price_whole = item.find("span", {"class": "a-price-whole"}).text
        
            price_fraction = item.find("span", {"class": "a-price-fraction"}).text
            
            item_list.append({"name": name, "price": price_whole + price_fraction})
        except:
            item_list.append({"name": name, "price": "No price available"})
        
  
    
    return item_list
    
@app.get("/items")
def get_data():
    return json.dumps(fetch_data(), ensure_ascii=False)

