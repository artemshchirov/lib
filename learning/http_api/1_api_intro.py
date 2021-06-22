# API - Application Programming Interface
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2021-05-19',
    'endtime': '2021-06-21',
    'latitude': '32.79',
    'longitude': '34.98',
    'maxradiuskm': '500'
})

# print(response.text)  # return type <str>
# print(response.json())  # return type <dict>

data = response.json()
print(data['type'])
print(data['features'][0]['properties']['place'])
print(data['features'][1]['properties']['place'])