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