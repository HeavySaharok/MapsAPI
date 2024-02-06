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
    address = f'https://static-maps.yandex.ru/1.x/'
    par = {
        'll': ll,
        'spn': spn,
        'l': appearance,
    }
    im = Image.open(BytesIO(requests.get(address, par).content))
    # Сохраняем в map.png
    im.save('map.png')
    im.close()
