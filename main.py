# annoying ass error handling
import os
import sys
class BrokenDependencyError(Exception): ...
try:
    import backup
    import textures
    import image_gen
    import gd_texture
    import enviroment
    import shutil
    import errors
    import docs
    
except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')
    raise BrokenDependencyError('Dependency does not exist, however the program has run a requirements.txt script ( try running the script again )')


if enviroment.QUALITY == 'reg':
    UQUALITY = ''
elif enviroment.QUALITY == 'hd':
    UQUALITY = '-hd'
elif enviroment.QUALITY == 'uhd':
    UQUALITY = '-uhd'
else:
    raise errors.InvalidQualityError(f'Quality variable can only be set to "reg", "hd" or "uhd" not "{enviroment.QUALITY}"')

RESOURCES_DICTIONARY = {
    
}

def randomiseTextures() -> None:
    print('Creating backups')
    backup.backupResourcesFolder(enviroment.GD_RESOURCES_PATH, 'backup/backup.zip')
    
    print('Generating AI Textures ( 1. SpriteSheet )')
    for resource_plist in RESOURCES_DICTIONARY:
        resource_png = RESOURCES_DICTIONARY[resource_plist]
        
        sheet = gd_texture.GDTexture(resource_plist, resource_png)
        
        print(f'  Plist file: {resource_plist}')
        print(f'  PNG file: {resource_png}\n')
        
        for i in sheet.get_plist_keys:
            coordinates = sheet.importTexture(i)
            
            print(f'    Generating Image [{i}]')
            iid = image_gen.requestAIImageGen(f'Generate me a sprite for Geometry Dash called {i}')
            uri = image_gen.getAIImageURL(iid)
            
            print(f'    Downloading image from {uri}')
            textures.downloadTextureImage(uri, i)
            print('    Resizing texture')
            textures.resizeTexture(i, coordinates)
            
            print(f'    Exporting texture [{i}]')
            sheet.exportTexture(i, (coordinates[0], coordinates[1]))
            
            print('')
    
        sheet.close()
    
    print('Generating AI Textures ( 2. Backgrounds, Grounds and Middlegrounds )')
    prefixes = {
        'background': {
            'indexes': (0, 59),
            
            'sizes': {
                'reg': (128, 128),
                'hd': (256, 256),
                'uhd': (512, 512) 
            }
        },
        
        'ground': {
            'indexes': (0, 22),
            
            'sizes': {
                'reg': (512, 512),
                'hd': (1024, 1024),
                'uhd': (2048, 2048) 
            }
        }
    }
    
    for i in range(prefixes['background']['indexes'][0], prefixes['background']['indexes'][1]):
        print(f'  Generating background: game_bg_{i}_001{UQUALITY}.png')
        coordinates = prefixes['background']['sizes'][enviroment.QUALITY]
        
        print('    Generating AI Image')
        iid = image_gen.requestAIImageGen(f'Generate me a Geometry Dash background called game_bg_{i}_001{UQUALITY}.png')
        uri = image_gen.getAIImageURL(iid)
        
        print('    Downloading and resizing image')
        textures.downloadTextureImage(uri, f'game_bg_{i}_001{UQUALITY}.png')
        textures.resizeTexture(uri, coordinates)
        
        print('    Exporting texture')
        shutil.move(f'game_bg_{i}_001{UQUALITY}.png', f'{enviroment.GD_RESOURCES_PATH}/game_bg_{i}_001{UQUALITY}.png')
        
        print('')
    
    for i in range(prefixes['ground']['indexes'][0], prefixes['ground']['indexes'][1]):
        print(f'  Generating ground: groundTile_{i}_001.png')
        coordinates = prefixes['background']['sizes'][enviroment.QUALITY]
        
        print('    Generating AI Image')
        iid = image_gen.requestAIImageGen(f'Generate me a Geometry Dash ground called groundTile_{i}_001.png')
        uri = image_gen.getAIImageURL(iid)
        
        print('    Downloading and resizing image')
        textures.downloadTextureImage(uri, f'groundTile_{i}_001.png')
        textures.resizeTexture(uri, coordinates)
        
        print('    Exporting texture')
        shutil.move(f'groundTile_{i}_001.png', f'{enviroment.GD_RESOURCES_PATH}/groundTile_{i}_001.png')
        shutil.move(f'groundTile_{i}_001.png', f'{enviroment.GD_RESOURCES_PATH}/groundTile_{i}_2_001.png')
        
        print('')
    
    print('Texture randomiser complete')

def documentation() -> None:
    print('Choose Docuement\n')
    print('1. License')
    print('2. Readme')
    print('3. Installer Guide')
    print('4. CODEOWNERS')
    
    cmd = int(input('\n> '))
    
    match cmd:
        case 1:
            docs.project_license()
        case 2:
            docs.readme()
        case 3:
            docs.installer_guide()
        case 4:
            docs.codeowners()

def main(argv: list) -> None:
    if argv[1] == 'randomise':
        match input('Are you shure (Y or n): ').lower():
            case 'y':
                randomiseTextures()
            case 'n':
                exit(0)
            case _:
                exit(0)
    
    elif argv[1] == 'documentation':
        documentation()

    elif argv[1] == 'extract':
        location = input('Backup location: ')
        backup.extractBackup(enviroment.GD_RESOURCES_PATH, location)


if __name__ == '__main__':
    main(sys.argv)
