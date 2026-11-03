import commandInterface
import json
import pathlib
import sys
import shutil

def initFileTreeSys():
    dirPath = pathlib.Path('./FTinit')
    dirPath.mkdir()

    (dirPath / 'FileDB').mkdir()

    shutil.copy(
        pathlib.Path('./FTetc/FileTreeConfigOrigin.json'),
        (dirPath / 'FileTreeConfig.json'))

    with (dirPath / 'Tree.json').open('w', encoding='utf-8') as file:
        json.dump({}, file)


def FileTreeInitProcess():
    dirPath = pathlib.Path('./FTinit')
    if (dirPath.is_dir()):
        print('exist')
    else:
        print('FTinit디렉터리가 존재하지 않습니다.')
        respond = input('FileTree를 초기화 하겠습니까? (y / n)')
        if (respond == 'y'):
            initFileTreeSys()
        else:
            sys.exit()
            

if __name__ == '__main__':
    FileTreeInitProcess()
    commandInterface.callCommandInterface()