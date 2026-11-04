import pathlib
import json

import TreeManager
import FileIO
import Utility

FileTreePath = pathlib.Path('./')


#help명령 처리 함수
def help(command):
    if (command[1] == 'commit'):
        txtFilePath = FileTreePath / 'FTetc/help-commit.txt'
        content = txtFilePath.read_text(encoding='utf-8')
    print(content)
    

#commit명령 처리 함수
def commit(command):
    print(1)
    #FileTreeConfig 업데이트
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    FTconfig['totalNodeCount'] += 1
    FTconfig['currentNode'] = f'N{FTconfig['totalNodeCount']}'
    Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
    print(2)
    TreeManager.addNode(command[1])
    print(3)