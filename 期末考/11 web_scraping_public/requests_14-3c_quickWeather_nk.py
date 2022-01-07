#! python3
# quickWeather.py - Prints the current weather for a location.

import json, requests,  pprint
from datetime import datetime

location = 'Taipei,TW'

# Download the JSON data from OpenWeatherMap.org's API
APIKey='放入你自己的APIKey'
url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q=%s&appid=%s' % (location, APIKey)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
#weatherData =  response.json()
pprint.pprint(weatherData)


# Print weather descriptions.
desc = weatherData['weather'][0]['description']
temp = weatherData['main']['temp']
date = datetime.fromtimestamp(weatherData['dt'])
#date_str = date.strftime('%Y-%m-%d %H:%M:%S')
date_str = date.strftime('%Y-%m-%d %I:%M %p') # 00:00 AM/PM

print('Current weather in %s:' % (location))
print('{:s} - {:s}, {:.2f}\u2103'.format(date_str, desc, temp))
print()

