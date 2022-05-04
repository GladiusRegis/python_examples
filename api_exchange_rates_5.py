from urllib.request import urlopen
from json import loads

with urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))
    rates = data[0]['rates']

    exchange = input('What value do you want to exchange into PLN? ')
    value, code = exchange.split(' ')
    value = float(value)

    # rate_lc = [rate for rate in rates if rate['code'] == code]
    rate = list(filter(lambda x: x['code'] == code, rates))
    print(f'You receive {value * rate[0]["mid"]} PLN ')

