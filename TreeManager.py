import datetime

import Utility


#node추가 코드
def addNode(commitMessage=''):
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')

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
        "commitDate": commitDate
    }

    #Tree 업데이트
    beforeTree = Utility.getJson('./FTinit/Tree.json')
    beforeTree[nodeName] = newNode
    Utility.dumpJson(beforeTree, './FTinit/Tree.json')