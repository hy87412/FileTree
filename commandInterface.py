import sys
import pathlib
import json

import FileTreeEngine


#명령어 인터페이스 호출
def callCommandInterface():
    FTconfigPath = pathlib.Path('./FTinit/FileTreeConfig.json')
    while True:
        
        with FTconfigPath.open('r', encoding='utf-8') as file:
            FTconfig = json.load(file)
            currentNode = FTconfig['currentNode']
            
        try:
            inputCommand = input(f'[{currentNode}]>>> ').split() #명령어 입력 및 분해
            if (inputCommand[0] == 'exit'): #>>> exit
                sys.exit()
            
            elif (inputCommand[0] == 'help'): #>>> help command
                if (inputCommand[1]):
                    FileTreeEngine.help(inputCommand)
                    
            elif (inputCommand[0] == 'commit'): #>>> commit message
                if (inputCommand[1]):
                    FileTreeEngine.commit(inputCommand)
                    
            elif (inputCommand[0] == 'goto'): # >>> goto nodeName
                if (inputCommand[1]):
                    FileTreeEngine.goto(inputCommand)
                    
            elif (inputCommand[0] == 'nodelist'):
                FileTreeEngine.nodeList()
            
            elif (inputCommand[0] == 'nodeinfo'):
                if (inputCommand[1]):
                    FileTreeEngine.nodeinfo(inputCommand[1])
            
            else: #명령어 없을시
                print('else') #debug
                print('올바른 명령어를 입력하세요.')
                
        except: #명령어 오류 예외처리
            print('except') #debug
            print('올바른 명령어를 입력하세요.')