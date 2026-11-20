
import pathlib
import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def visualizeTree(tree, currentNode, filename='FileTree.png'):
    # 한글 폰트 설정 (Windows)
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    # 노드 위치 저장
    positions = {}
    visited = set()
    leafCount = 0

    # 트리의 노드 위치 계산
    def calculatePosition(nodeName, depth=0):
        nonlocal leafCount

        if nodeName in visited or nodeName not in tree:
            return None

        visited.add(nodeName)

        children = tree[nodeName]['childNodes']
        childPositions = []

        for child in children:
            childPosition = calculatePosition(child, depth + 1)

            if childPosition is not None:
                childPositions.append(childPosition)

        # 자식이 없는 노드
        if not childPositions:
            x = leafCount * 2.5
            leafCount += 1

        # 부모 노드는 자식 노드들의 중앙에 배치
        else:
            x = sum(childPositions) / len(childPositions)

        positions[nodeName] = (x, -depth)

        return x

    # root부터 위치 계산
    calculatePosition('root')

    # 그래프 크기 계산
    maxDepth = max(
        (abs(y) for x, y in positions.values()),
        default=0
    )

    figWidth = max(8, leafCount * 2.5)
    figHeight = max(4, (maxDepth + 1) * 1.8)

    fig, ax = plt.subplots(figsize=(figWidth, figHeight))

    ax.axis('off')

    # 연결선 그리기
    for nodeName, nodeData in tree.items():
        if nodeName not in positions:
            continue

        parentNode = nodeData['parentNode']

        if parentNode and parentNode in positions:
            parentX, parentY = positions[parentNode]
            childX, childY = positions[nodeName]

            ax.plot(
                [parentX, childX],
                [parentY - 0.35, childY + 0.35],
                color='#A0A0A0',
                linewidth=1.5,
                zorder=1
            )

    # 노드 그리기
    for nodeName, nodeData in tree.items():
        if nodeName not in positions:
            continue

        x, y = positions[nodeName]

        # 노드 색상 결정
        if nodeName == currentNode:
            faceColor = '#D5F5DF'
            edgeColor = '#269653'
        elif nodeData['isPined'] == 'True':
            faceColor = '#FFF0C2'
            edgeColor = '#D69E36'
        else:
            faceColor = '#E8EEF7'
            edgeColor = '#5579A8'

        # 노드 라벨 구성
        message = nodeData['commitMessage']

        if message:
            message = textwrap.fill(message, width=18)
            label = f'{nodeName}\n{message}'
        else:
            label = nodeName

        if nodeData['isPined'] == 'True':
            label += '\n[PIN]'

        # 노드 박스 생성
        nodeBox = FancyBboxPatch(
            (x - 0.85, y - 0.35),
            1.7,
            0.7,
            boxstyle='round,pad=0.08',
            facecolor=faceColor,
            edgecolor=edgeColor,
            linewidth=2 if nodeName == currentNode else 1.5,
            zorder=2
        )

        ax.add_patch(nodeBox)

        # 노드 텍스트
        ax.text(
            x,
            y,
            label,
            ha='center',
            va='center',
            fontsize=9,
            zorder=3
        )

    # 그래프 여백
    if positions:
        xs = [x for x, y in positions.values()]
        ys = [y for x, y in positions.values()]

        ax.set_xlim(min(xs) - 1.5, max(xs) + 1.5)
        ax.set_ylim(min(ys) - 1, max(ys) + 1)

    ax.set_title('FileTree Commit History', fontsize=15, pad=20)

    # PNG 저장
    outputPath = pathlib.Path(filename)

    fig.savefig(
        outputPath,
        dpi=200,
        bbox_inches='tight',
        facecolor='white'
    )

    plt.close(fig)

    print(f'트리 이미지 생성 완료: {outputPath.resolve()}')
