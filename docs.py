def __readfile(file: str) -> None:
    with open(file) as rstream:
        print(rstream.read())

def project_license() -> None:
    __readfile('license.txt')

def readme() -> None:
    __readfile('readme.md')

def installer_guide() -> None:
    __readfile('installer_guide.md')

def codeowners() -> None:
    __readfile('.github/CODEOWNERS')