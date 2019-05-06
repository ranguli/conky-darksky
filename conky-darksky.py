#!/usr/bin/python
import requests
from decouple import config 

DARK_SKY_API_KEY = config('DARK_SKY_API_KEY')

# Free geoip API that allows 15,000 requests an hour. Returns our external IP
response = requests.get('https://freegeoip.app/json')

if response.status_code == requests.codes.ok:
    # People say I have a bad latitude sometimes - HAHA, get it
    latitude = response.json().get('latitude')
    longitude = response.json().get('longitude')
    lat_long = str(latitude) + "," + str(longitude)
    city = response.json().get('city')
else:
    with open('.conky-darksky', 'w+') as f:
        for item in out:
            f.write(str(":(" + response.status.code) + '\n')
   exit()

# Weather API with 1,000 free calls per day. 
url = 'https://api.darksky.net/forecast' + '/' + DARK_SKY_API_KEY + '/' + lat_long
response = requests.get(url)
response = response.json().get('currently')

temp_fahrenheit = int(response['temperature'])
temp_celcius = int((temp_fahrenheit - 32) * (5/9))
wind_miles = int(response['windSpeed'])
wind_kilometres = int(wind_miles * 1.609)

out = [
    city,
    response['summary'],
    response['icon'],
    temp_celcius,
    temp_fahrenheit,
    wind_kilometres,
    wind_miles,
]

with open('.conky-darksky', 'w+') as f:
    for item in out:
        f.write(str(item) + '\n')