import requests
import math

def get_temp(city_name, lat, lon, api_key):
    # Send GET request
    # Put response in rep variable
    rep = requests.get(
        'https://api.openweathermap.org/data/2.5/forecast?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key)
    # Put json from the response in json variable
    json = rep.json()
    # Print the city name
    print('Weather in ' + city_name + ' : ')
    # Initialize temp list
    temp = []
    for weather in json['list']:
        temp.append(math.trunc(weather['main']['temp'] - 273))
    # Find and display minimum temperature
    print(' - Minimum temperature for 5 days : ' + str(min(temp)) + '°C')
    # Find and display maximum temperature
    print(' - Maximum temperature for 5 days : ' + str(max(temp)) + '°C')

if __name__ == '__main__':
    # Get weather in Toulouse
    get_temp('Toulouse', 43.6000, 1.4333, '344e1eb4f37ada7d4c994e4e760f05fb')
    # Get weather in Saint-Geours-de-Maremne
    get_temp('Saint-Geours-de-Maremne', 43.6833, -1.2333, '344e1eb4f37ada7d4c994e4e760f05fb')
    # Get weather in Mérignac
    get_temp('Mérignac', 44.8459, -0.6552, '344e1eb4f37ada7d4c994e4e760f05fb')