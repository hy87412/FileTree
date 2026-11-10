import pathlib
import sys
import shutil
import datetime

import commandInterface
import Utility

#FTinit dir없을시 초기화 함수
def initFileTreeSys():
    print('FTinit/ 생성중...')
    dirPath = pathlib.Path('./FTinit')
    dirPath.mkdir()

    print('FTinit/FileDB/ 생성중...')
    (dirPath / 'FileDB').mkdir()

    print('FTinit/FileTreeConfig.json 복사중...')
    shutil.copy(
        pathlib.Path('./FTetc/FileTreeConfigOrigin.json'),
        (dirPath / 'FileTreeConfig.json'))

    print('FTinit/Tree.json 생성중...')
    treeJson = Utility.getJson('./FTetc/TreeOrigin.json')
    treeJson['root']['commitDate'] = f'{datetime.datetime.now()}'
    Utility.dumpJson(treeJson, './FTinit/Tree.json')
    
    print('FileTree초기화 완료!')

#init과정 수행 함수
def FileTreeInitProcess():
    dirPath = pathlib.Path('./FTinit')
    if (dirPath.is_dir()):
        print('exist')
    else:
        print('FTinit디렉터리가 존재하지 않습니다.')
        respond = input('FileTree를 초기화 하겠습니까? (y / n) >>> ')
        if (respond == 'y'):
            initFileTreeSys()
        else:
            sys.exit()
            

if __name__ == '__main__':
    print('FileTree 실행중...')
    FileTreeInitProcess()
    commandInterface.callCommandInterface()