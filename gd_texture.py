import shutil
import plistlib
import os
from PIL import Image

class GDTexture:
    def __init__(self, plist_file: str, spritesheet: str) -> None:
        self.plist = plist_file
        self.sheet = spritesheet
        
        shutil.copyfile(plist_file, 'spritesheet.plist')
        shutil.copyfile(spritesheet, 'spritesheet.png')
    
    def reinit(self, plist_file: str, spritesheet: str) -> None:
        self.plist = plist_file
        self.sheet = spritesheet
        
        shutil.copyfile(plist_file, 'spritesheet.plist')
        shutil.copyfile(spritesheet, 'spritesheet.png')
    
    def close(self) -> None:
        os.remove('spritesheet.plist')
        os.remove('spritesheet.png')
    
    @property
    def get_plist_keys(self) -> list:
        return_array = []
        with open(self.plist, 'rb') as file:
            plist = plistlib.load(file)
        for i in plist['frames']:
            return_array.append(i)
        return return_array
    
    def importTexture(self, name: str) -> tuple:
        with open(self.plist, 'rb') as file:
            plist = plistlib.load(file)
        
        # Coordinates system
        texture_rect: str = plist['frames'][name]['textureRect']
        
        texture_rect = texture_rect.removeprefix('{{')
        texture_rect = texture_rect.removesuffix('}}')
        texture_rect = texture_rect.split('},{')
        texture_rect[0] = texture_rect[0].split(',')
        texture_rect[1] = texture_rect[1].split(',')
        
        return int(texture_rect[0][1]), int(texture_rect[1][0])+int(texture_rect[0][0]), int(texture_rect[1][1])+int(texture_rect[0][1])
    
    def exportTexture(self, file: str, coordinates: tuple[int, int]) -> None:
        insertImage = Image.open(self.sheet)
        importImage = Image.open(file)
        
        for i in range(importImage.size[0]):
            for ii in range(importImage.size[1]):
                insertImage.putpixel((i+coordinates[0], ii+coordinates[1]), importImage.getpixel(i, ii))
        
        insertImage.save(self.sheet)