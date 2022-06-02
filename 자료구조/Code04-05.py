## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end='   ')
    while (current.link != None):
        current = current.link
        print(current.data, end='   ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current
    # 첫 노드 앞에 삽입... 예 : 다현, 화사
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return

    # 중간 노드 삽입... 예: 사나, 솔라
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막 노드 삽입 (=findData 없음).. 예: 민중, 문별
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # 첫 노드를 삭제할 때.... 예: 다현
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
        return

    # 첫 노드 외의 노드 삭제... 예: 쯔위
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return


def findNode(findData):
    global memory, head, pre, current
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()


## 전역
memory = []
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
node = Node()   # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:  #  ['정연', '쯔위', .....]
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)

# insertNode('사나', '솔라')
# printNodes(head)

# insertNode('민중', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)

# deleteNode('쯔위')
# printNodes(head)

# fNode = findNode('쯔위')
# print(fNode.data)