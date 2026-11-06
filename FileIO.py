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
    print(1)
    loadFileHashList = tree[nodeName]['fileHashes']
    print(2)
    fileDBPath = pathlib.Path('./FTinit/FileDB')
    print(3)
    for fileHash in loadFileHashList:
        print(4)
        targetFileDirPath = pathlib.Path('./FTinit/FileDB/' + fileHash)
        print(5)
        targetFilePath = next(targetFileDirPath.iterdir())
        print(6)
        destinationPath = parentDirPath / targetFilePath.name

        print(7)
        shutil.copy(
            targetFilePath,
            destinationPath
        )
        print(8)
        
        
