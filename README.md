# FileTree

## 주요 기능

1. **commit (message)** 명령어를 통하여 FileTree의 부모디렉터리의 파일을 저장하고 현재상태의 정보를 담은 노드를 생성할수 있습니다.

2. **goto (targetnode)** 명령어를 통하여 지정한 targetnode 로 이동하여 FileTree의 부모디렉터리의 파일을 갈려는 노드의 상태로 변경합니다.

3. **nodelist** 명령어를 통하여 현재 존재하는 노드들의 정보를 출력합니다.

4. **nodeinfo (targetnode)** targetnode의 상세한 정보를 출력합니다.

5. **status** 현재 상태를 출력합니다.

6. **setpin** 현재 노드에 pin을 지정합니다.

7. **delpin** 현재 노드의 pin을 제거합니다.

8. **opti** pin으로 지정된 노드를 제외한 모든노드를 삭제하고 트리를 재구성합니다.

9. **tv** 현재의 트리구조를 시각화하여 .png파일을 FileTree의 부모디렉터리에 저장합니다.


## 사용법

- FileTree디렉터리 내의 start.bat실행.

- FTinit 디렉터리가 최초실행전 존재하는 경우 삭제.

- FileTree를 초기화 시키고 싶으면 FTinit디렉터리 삭제.

### 실행이 안될때

- FileTree는 matplotlib라이브러리를 필요로 합니다. matplotlib이 존재하지 않는경우 오류가 발생할수 있습니다.

    > pip install matplotlib

