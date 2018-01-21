import requests
url = 'https://rest.coinapi.io/v1/symbols'
headers = {'X-CoinAPI-Key' : 'E833AC5B-7E68-4093-BA69-4B95175A3CAD'}
response = requests.get(url, headers=headers)
print(response.content)