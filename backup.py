from zipfile import ZipFile
import os
import shutil

def backupResourcesFolder(res: str, file: str) -> None:
    zipfile = ZipFile(file, 'w')
    
    for i in os.listdir(res):
        zipfile.write(f'{res}/{i}')

def extractBackup(res: str, file: str) -> None:
    shutil.rmtree(res)
    os.mkdir(res)
    
    ZipFile(file).extractall(res)