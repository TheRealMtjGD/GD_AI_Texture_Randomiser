import requests
from PIL import Image

def downloadTextureImage(uri: str, texture: str) -> None:
    with open(texture, 'wb') as file:
        file.write(requests.get(uri).content)

def resizeTexture(texture: str, coordinates: tuple) -> None:
    Image.open(texture).resize((coordinates[0], coordinates[1]), box=coordinates).save(texture)