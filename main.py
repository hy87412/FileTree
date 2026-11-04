import pathlib
import sys
import shutil
import datetime

import commandInterface
import Utility

#FTinit dir없을시 초기화 함수
def initFileTreeSys():
    dirPath = pathlib.Path('./FTinit')
    dirPath.mkdir()

    (dirPath / 'FileDB').mkdir()

    shutil.copy(
        pathlib.Path('./FTetc/FileTreeConfigOrigin.json'),
        (dirPath / 'FileTreeConfig.json'))

    treeJson = Utility.getJson('./FTetc/TreeOrigin.json')
    treeJson['root']['commitDate'] = f'{datetime.datetime.now()}'
    Utility.dumpJson(treeJson, './FTinit/Tree.json')

#init과정 수행 함수
def FileTreeInitProcess():
    dirPath = pathlib.Path('./FTinit')
    if (dirPath.is_dir()):
        print('exist')
    else:
        print('FTinit디렉터리가 존재하지 않습니다.')
        respond = input('FileTree를 초기화 하겠습니까? (y / n) >>>')
        if (respond == 'y'):
            initFileTreeSys()
        else:
            sys.exit()
            

if __name__ == '__main__':
    FileTreeInitProcess()
    commandInterface.callCommandInterface()