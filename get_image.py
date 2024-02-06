import requests
from PIL import Image
from io import BytesIO


def get_image(ll: str, spn: str, appearance: str):
    """
    Генерирует изображение заданной территории
    :param ll: Ширина и долгота.
    :param spn: Угловые размеры.
    :param appearance: Слой.
    """
    if appearance == 'satellite':
        vid = 'sat'
    elif appearance == 'scheme':
        vid = 'map'
    else:
        vid = 'sat,skl'
    address = f'https://static-maps.yandex.ru/1.x/'
    par = {
        'll': ll,
        'spn': spn,
        'l': vid
    }
    im = Image.open(BytesIO(requests.get(address, par).content))
    # Сохраняем в map.png
    im.save('map.png')
    im.close()
