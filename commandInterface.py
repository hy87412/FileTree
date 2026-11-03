import sys
import pathlib

import FileTreeEngine

def callCommandInterface():
    while True:
        commandPath = pathlib.Path('./')
        try:
            inputCommand = input(f'[{commandPath.resolve()}]>>> ').split()
            if (inputCommand[0] == 'exit'):
                sys.exit()
            
            elif (inputCommand[0] == 'help'):
                if (inputCommand[1]):
                    FileTreeEngine.help(inputCommand)
                    
            # elif (inputCommand[0] == 'commit'):
            #     if (inputCommand[1]):
            #         FileTreeEngine.commit(inputCommand)
                
            
            else:
                print('else')
                print('올바른 명령어를 입력하세요.')
                
        except:
            print('except')
            print('올바른 명령어를 입력하세요.')