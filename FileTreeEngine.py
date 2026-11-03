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
    

# def commit(command):
    