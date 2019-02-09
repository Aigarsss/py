#! python3
# python quickWeather.py Oslo

# Overall, the program does the following:
# Reads the requested location from the command line.
# Downloads JSON weather data from OpenWeatherMap.org.
# Converts the string of JSON data to a Python data structure.
# Prints the weather for today and the next two days.

# So the code will need to do the following:
# Join strings in sys.argv to get the location.
# Call requests.get() to download the weather data.
# Call json.loads() to convert the JSON data to a Python data structure.
# Print the weather forecast.

import sys, json, requests

# Get locatin from command line arguments
if len(sys.argv) > 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWearherMap.org API
key = 'xxx' # get it from the web page
url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid='.format(location) + key
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable
weatherData = json.loads(response.text)
# Print weather descriptions
w = weatherData['list']
print('Current weather in {}:'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('3h later:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('3h later')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
