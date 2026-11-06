import pathlib

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
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    respond = True
    isChanged = True

    if FTconfig['currentNode'] != 'root':
        if not(Utility.isParentDirFileChanged()):
            print('변경사항이 존재하지 않습니다.')
            isChanged = False
            respond = input('계속 commit하시겠습니까? (y / n) >>> ')
            if (respond != 'y'):
                respond = False

    if respond:
        #FileTreeConfig 업데이트
        FTconfig['totalNodeCount'] += 1
        Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
        TreeManager.addNode(command[1])
        if isChanged:
            FileIO.addInnerDirFilesToFileDB()
        FTconfig['currentNode'] = f'N{FTconfig['totalNodeCount']}'
        Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
        
        
#goto명령 처리 함수
def goto(command):
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    tree = Utility.getJson('./FTinit/Tree.json')

    if (command[1] in tree.keys()):
        FTconfig['currentNode'] = command[1]
        FileIO.syncToChangedNode(command[1])
        
        Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
    else:
        print('node가 존재하지 않습니다.')