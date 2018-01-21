#from bs4 import BeautifulSoup
#soup = BeautifulSoup(page.content, 'html.parser')
import requests
from bs4 import BeautifulSoup

coins = ["tron","verge","dogecoin"]
#coins = ["tron"]

url = "https://coinmarketcap.com/currencies/"


def current_value( var, coin ):
    if coin == "tron":
        return( var * 396 )
    if coin == "verge":
        return( var * 296 )
    if coin == "dogecoin":
        return( var * 4000 )
    
for coin in coins:
        page = requests.get(url+coin)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        c_val = soup.find("span", class_="text-large2").text
        #print(c_val)
        val = current_value( float(c_val), coin)
        print(val)
#print(soup.prettify())
