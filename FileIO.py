import pathlib
import shutil

import Utility


def addFileToFileDB(stringFilePath):
    filePath = pathlib.Path(stringFilePath)
    fileHash = Utility.getHash(stringFilePath)
    dirPath = pathlib.Path('./FTinit/FileDB/' + fileHash)
    
    #디렉터리가 존재하지 않을때만 add
    if not(dirPath.exists()):
        dirPath.mkdir()
        shutil.copy(filePath, (dirPath / filePath.name))
    

def addInnerDirFilesToFileDB():
    parentDirPath = pathlib.Path('../')
    for filePath in parentDirPath.iterdir():
        if filePath.is_file():
            addFileToFileDB(str(filePath))
            

def syncToChangedNode(nodeName):
    FTconfig = Utility.getJson('./FTinit/FileTreeConfig.json')
    tree = Utility.getJson('./FTinit/Tree.json')
    
    fileHashList = tree[nodeName]['fileHashes']
    
    #부모 디렉터리 파일 전체 삭제
    parentDirPath = pathlib.Path('../')
    for filePath in parentDirPath.iterdir():
        if filePath.is_file():
            filePath.unlink()
            
    loadFileHashList = tree[nodeName]['fileHashes']
    fileDBPath = pathlib.Path('./FTinit/FileDB')
    
    for fileHash in loadFileHashList:
        targetFileDirPath = pathlib.Path('./FTinit/FileDB/' + fileHash)
        targetFilePath = next(targetFileDirPath.iterdir())
        destinationPath = parentDirPath / targetFilePath.name
        shutil.copy(
            targetFilePath,
            destinationPath
        )
        
        
def deleteHashDirExceptPined():
    tree = dict(Utility.getJson('./FTinit/Tree.json'))
    hashes = set()
    pinedHashes = set()
    notPinedHashes = set()

    nodeList = tree.keys()
    for node in nodeList:
        hashes |= set(tree[node]['fileHashes'])
        if tree[node]['isPined'] == 'True':
            pinedHashes |= set(tree[node]['fileHashes'])
            
    notPinedHashes = hashes - pinedHashes
    print(hashes)
    print(pinedHashes)
    print(notPinedHashes)
    for hash in notPinedHashes:
        hashFileDir = pathlib.Path('./ftinit/FileDB/' + hash)
        print(hashFileDir)
        shutil.rmtree(hashFileDir)