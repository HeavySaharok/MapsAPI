import requests


def locate(name):
    address = 'http://geocode-maps.yandex.ru/1.x/'
    pars = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
            'geocode': name,
            'format': 'json'
            }
    resp = requests.get(address, pars).json()
    first_result = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    return ','.join(first_result['Point']['pos'].split(' '))
