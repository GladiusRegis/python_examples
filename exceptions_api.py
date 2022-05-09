from json import load
from urllib.request import urlopen

with urlopen('https://restcountries.com/v3.1/name/poland') as response:
    data = response.read().decode('utf-8')
    print(data)
