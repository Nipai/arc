import requests
from bs4 import BeautifulSoup as bs
import json

#links
sonos_url = 'https://www.sonos.com/nl-nl/shop/arc-black?gclid=Cj0KCQjww4OMBhCUARIsAILndv5e0K3724isQzPmphESAVUx8Z10BqyzNMuDewT3YE9i3pqmGFHELYoaAoWsEALw_wcB&gclsrc=aw.ds'
expert_url = 'https://www.expert.nl/sonos-arc-zwart'
#does not want to work
plattetv_url = 'https://www.plattetv.nl/product/sonos-arc-zwart?channable=0324076964003234343233d0&utm_campaign=Google&utm_content=Listing&utm_source=Google&utm_medium=shopping&utm_term=Sonos+Arc+Zwart&ad_id=465784161753&gclid=Cj0KCQjww4OMBhCUARIsAILndv58raEfzc-H6w6IZpSGH4LIjFTLNFl6pTWO1bpGKmQTwpSJlz6juLIaAmXGEALw_wcB'
mediamarkt_url = 'https://www.mediamarkt.nl/nl/product/_sonos-arc-zwart-1661502.html'

sonos = requests.get(sonos_url)
expert = requests.get(expert_url)
#plattetv = requests.get(plattetv_url)
mediamarkt = requests.get(mediamarkt_url)

sonos_soup = bs(sonos.text, 'html.parser')
sonos_price = float(sonos_soup.find_all('meta', attrs={'name':'og:price:amount'})[0].get('content'))

expert_soup = bs(expert.text, 'html.parser')
expert_price = float(expert_soup.find_all('p', attrs={'class': 'price'})[0].getText().strip(',-'))

mediamarkt_soup = bs(mediamarkt.text, 'html.parser')
mediamart_price = float(mediamarkt_soup.find_all('meta', attrs={'property' : "product:price:amount"})[0].get('content'))

x = {'Sonos': sonos_price, 'Expert':expert_price, 'Mediamarkt':mediamart_price}

print(x)
