import hashlib
import pathlib
import json

def getHash(stringPath):
    filePath = pathlib.Path(stringPath)
    data = filePath.read_bytes()

    header = f"blob {len(data)}\0".encode('utf-8')

    return hashlib.sha1(header + data).hexdigest()


def getJson(stringPath):
    jsonPath = pathlib.Path(stringPath)
    with jsonPath.open('r', encoding='utf-8') as file:
        jsonFile = json.load(file)
    return jsonFile


def dumpJson(jsonFile, stringTargetPath):
    with (pathlib.Path(stringTargetPath)).open('w', encoding='utf-8') as file:
        json.dump(jsonFile, file, ensure_ascii=False, indent=4)
        

def getFilesHashList(stringDirPath):
    dirPath = pathlib.Path(stringDirPath)
    hashList = []
    for filePath in dirPath.iterdir():
        if filePath.is_file():
            hashList.append(getHash(str(filePath)))
    return hashList