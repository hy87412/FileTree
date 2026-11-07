import datetime

import Utility


#node추가 코드
def addNode(commitMessage=''):
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    treeFile = Utility.getJson('./FTinit/Tree.json')
    
    #새 노드 요소구성
    nodeName = f'N{FTconfig['totalNodeCount']}'
    parentNode = FTconfig['currentNode']
    fileHashes = Utility.getFilesHashList('../')
    commitDate = str(datetime.datetime.now())

    newNode = {
        "commitMessage": commitMessage,
        "fileHashes": fileHashes,
        "parentNode": parentNode,
        "childNodes": [],
        "commitDate": commitDate,
        "isPined": "False"
    }

    #자식노드 추가
    treeFile[parentNode]['childNodes'].append(nodeName)
    
    #Tree 업데이트
    treeFile[nodeName] = newNode
    Utility.dumpJson(treeFile, './FTinit/Tree.json')


def setPin(targetNode):
    tree = Utility.getJson('./FTinit/Tree.json')

    tree[targetNode]['isPined'] = 'True'
    
    Utility.dumpJson(tree, './FTinit/Tree.json')


def delPin(targetNode):
    tree = Utility.getJson('./FTinit/Tree.json')
    
    tree[targetNode]['isPined'] = 'False'
    
    Utility.dumpJson(tree, './FTinit/Tree.json')