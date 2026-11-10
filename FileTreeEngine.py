import pathlib

import TreeManager
import FileIO
import Utility

FileTreePath = pathlib.Path('./')


def updateConfig():
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    tree = Utility.getJson('./FTinit/Tree.json')

    #pin정보 업데이트
    FTconfig['isCurrentNodePined'] = tree[FTconfig['currentNode']]['isPined']

    Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')


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
        FTconfig['isCurrentNodePined'] = 'False'
        Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
        
        
#goto명령 처리 함수
def goto(command):
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    tree = Utility.getJson('./FTinit/Tree.json')
    
    if (command[1] in tree.keys()):
        respond = 'y'
        if Utility.isParentDirFileChanged():
            print('변경사항을 commit하지 않았습니다.')
            respond = input('계속하시겠습니까? (y / n) >>> ')
        
        if (respond == 'y'):
            FTconfig['currentNode'] = command[1]
            FTconfig['isCurrentNodePined'] = tree[command[1]]['isPined']
            FileIO.syncToChangedNode(command[1])
        
            Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
            
    else:
        print('node가 존재하지 않습니다.')
        
        
#nodelist명령 처리 함수
def nodeList():
    tree = dict(Utility.getJson('./FTinit/Tree.json'))
    print('=' * 99)
    print(f'{"노드이름":11} {"pin":14} {"부모노드":11} {"자식노드":21} {"생성날짜"}')
    for nodeName in tree.keys():
        print(
            f'{nodeName:15} '
            f'{str(tree[nodeName]['isPined']):15}'
            f'{str(tree[nodeName]['parentNode']):15} '
            f'{str(tree[nodeName]['childNodes']):25} '
            f'{str(tree[nodeName]['commitDate'])}'
        )
    print('=' * 99)


#nodeinfo명령 처리 함수
def nodeinfo(nodeName):
    tree = dict(Utility.getJson('./FTinit/Tree.json'))
    
    if (nodeName in tree):
        nodeData = tree[nodeName]
        print(f'{'nodeName':15} : {nodeName}')
        print(f'{'commitMessage':15} : {nodeData['commitMessage']}')
        print(f'{'parentNode':15} : {nodeData['parentNode']}')
        print(f'{'childNodes':15} : {nodeData['childNodes']}')
        print(f'{'commitDate':15} : {nodeData['commitDate']}')
        print(f'{'isPined':15} : {nodeData['isPined']}')
        

#status명령 처리 함수
def status():
    FTconfig = dict(Utility.getJson('./FTinit/FileTreeConfig.json'))
    tree = dict(Utility.getJson('./FTinit/Tree.json'))
    currentNode = FTconfig['currentNode']
    
    nodeData = tree[currentNode]
    print(f'{'currentNode':15} : {currentNode}')
    print(f'{'commitMessage':15} : {nodeData['commitMessage']}')
    print(f'{'parentNode':15} : {nodeData['parentNode']}')
    print(f'{'childNodes':15} : {nodeData['childNodes']}')
    print(f'{'commitDate':15} : {nodeData['commitDate']}')
    
    
#setpin명령 처리 함수
def setPin():
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    
    FTconfig['isCurrentNodePined'] = 'True'
    TreeManager.setPin(FTconfig['currentNode'])
    
    Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')


#delpin명령 처리함수
def delPin():
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    
    if (FTconfig['currentNode'] != 'root'):
        FTconfig['isCurrentNodePined'] = 'False'
        TreeManager.delPin(FTconfig['currentNode'])
        
        Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
    else:
        print('root노드의 핀은 제거할수 없습니다.')


#opti명령 처리함수
def opti():
    tree = Utility.getJson('./FTinit/Tree.json')
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')

    if FTconfig['isCurrentNodePined'] == 'True':
        respond = input('핀하지 않은 노드는 삭제됩니다.\n계속하시겠습니까? (y / n) >>> ')
        if respond == 'y':
            tree = TreeManager.recreatePinedTree(tree)
            FileIO.deleteHashDirExceptPined()
        
            Utility.dumpJson(tree, './FTinit/Tree.json')
            Utility.dumpJson(FTconfig, './FTinit/FileTreeConfig.json')
    else:
        print('opti는 핀이 되어있는 노드에서만 사용할수 있습니다.')
