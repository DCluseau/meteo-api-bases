import requests
import math

if __name__ == '__main__':
    # Get weather in Toulouse
    rep = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=43.6000&lon=1.4333&appid=344e1eb4f37ada7d4c994e4e760f05fb')
    json = rep.json()
    print('Weather in Toulouse')
    temp = []
    for weather in json['list']:
        temp.append(math.trunc(weather['main']['temp'] - 273))
    print(' - Minimum temperature for 5 days : ' + str(min(temp)) + '°C')
    print(' - Maximum temperature for 5 days : ' + str(max(temp)) + '°C')

    # Get weather in Saint Geours
    temp = []
    rep = requests.get(
        'https://api.openweathermap.org/data/2.5/forecast?lat=-1.2333&lon=1.4333&appid=344e1eb4f37ada7d4c994e4e760f05fb')
    json = rep.json()
    print('Weather in Saint Geours')
    for weather in json['list']:
        temp.append(math.trunc(weather['main']['temp'] - 273))
    print(' - Minimum temperature for 5 days : ' + str(min(temp)) + '°C')
    print(' - Maximum temperature for 5 days : ' + str(max(temp)) + '°C')

    # Get weather in Mérignac
    rep = requests.get(
        'https://api.openweathermap.org/data/2.5/forecast?lat=44.8333&lon=-0.6333&appid=344e1eb4f37ada7d4c994e4e760f05fb')
    json = rep.json()
    temp = []
    print('Weather in Mérignac')
    for weather in json['list']:
        temp.append(math.trunc(weather['main']['temp'] - 273))
    print(' - Minimum temperature for 5 days : ' + str(min(temp)) + '°C')
    print(' - Maximum temperature for 5 days : ' + str(max(temp)) + '°C')