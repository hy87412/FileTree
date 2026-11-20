import pathlib
import shutil
import os
import stat

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


def handleRemoveReadonly(func, path, excInfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def deleteHashDirExceptPined():
    tree = dict(Utility.getJson('./FTinit/Tree.json'))
    
    hashes = set()
    pinedHashes = set()

    for node in tree:
        hashes |= set(tree[node]['fileHashes'])
        if tree[node]['isPined'] == 'True':
            pinedHashes |= set(tree[node]['fileHashes'])

    notPinedHashes = hashes - pinedHashes

    for hash in notPinedHashes:
        hashFileDir = pathlib.Path('./FTinit/FileDB') / hash

        if hashFileDir.exists():
            try:
                shutil.rmtree(hashFileDir, onerror=handleRemoveReadonly)

            except PermissionError as e:
                print(f'삭제 실패: {hashFileDir}')
                print(e)