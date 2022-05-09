from json import loads
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


country = input('Enter country: ')
try:
    with urlopen(f'https://restcountries.com/v3.1/name/{country}') as response:
        data = loads(response.read().decode('utf-8'))
        # print(data)
        country_data = data[0]['capital'][0]
        print('Capital', country_data)
except (URLError, HTTPError) as error:
    print('Connection error')
