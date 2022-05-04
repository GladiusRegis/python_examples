from urllib.request import urlopen
from json import loads

URL = 'https://danepubliczne.imgw.pl/api/data/synop'

with urlopen(URL) as file:
    data = loads(file.read().decode('utf-8'))
    # print(data)
    city = input('For which city to check the weather information?: ')
    # weather_l = list(filter(lambda x: x['stacja'] == city, data))
    weather = [info for info in data if info['stacja'] == city]
    # print(weather_l)
    # print(weather)
    if len(weather) == 0:
        print('There is no weather station in this town, please enter another city nearby.')
    else:
        temperature = weather[0]['temperatura']
        air_pressure = weather[0]['cisnienie']
        wind_speed = weather[0]['predkosc_wiatru']
        rainfall = weather[0]['suma_opadu']
        humidity = weather[0]['wilgotnosc_wzgledna']

        print(f'City: {city}\n temp.: {temperature}\n air pressure: {air_pressure}')
        print(f' wind speed: {wind_speed}\n rainfall: {rainfall}\n humidity: {humidity}')
