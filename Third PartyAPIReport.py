import requests
import json


url= "https://any-api.com/ebay_com/buy_browse/docs/API_Description"
response = requests.get(url)
data = response.json()

filename = 'handbagreport.json'
f = open(filename, 'w')
json.dump(data, f indent=4)
