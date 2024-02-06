import requests
from PIL import Image
from io import BytesIO


def get_image(ll, spn):
    address = f'https://static-maps.yandex.ru/1.x/'
    par = {
        'll': ll,
        'spn': spn,
        'l': 'map',
    }
    im = Image.open(BytesIO(requests.get(address, par).content))
    im.save('map.png')
    im.close()

