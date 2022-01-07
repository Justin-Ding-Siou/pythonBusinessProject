#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json
import requests
import pprint

location = 'Taipei,TW'

# Download the JSON data from OpenWeatherMap.org's API
APIKey='放入你自己的APIKey'
url = 'http://api.openweathermap.org/data/2.5/forecast?units=metric&q=%s&appid=%s' % (location, APIKey)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
#weatherData = json.loads(response.text)
weatherData = response.json()
#pprint.pprint(weatherData)
#print(weatherData)

# Print weather descriptions.
wd = weatherData['list']
print(wd[0])
print('5 Day weather forecast in %s:' % (location))
#print(wd[0])
for w in wd:
    #print(w['dt_txt'],'-', str(w['main']['temp']) + ', ', w['weather'][0]['description'])
    print('{:s} - {:.2f}\u2103 {:s}'.format(w['dt_txt'], w['main']['temp'], w['weather'][0]['description']))
print()

