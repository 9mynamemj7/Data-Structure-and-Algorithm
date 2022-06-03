# 자료구조

> 알고리즘은 요리법, 자료구조는 재료
> 

# 강의 계획

- 메모
    
    ![Untitled](Untitled.png)
    

## 수업 목표

- 자료구조 및 알고리즘에 대한 개념 이해
- 파이썬 코딩을 통한 알고리즘 구현

## 교육 내용

- 자료구조 기본 개념
- 기본 알고리즘
- 파이썬 프로그래밍
- 현업 알고리즘 문제 테스트

---

# 1장, 자료구조의 개념과 종류

## 자료구조의 종류

1. 단순 자료구조
- 정수
- 실수
- 문자
- 문자열
2. ***선형 자료구조***
- 리스트
- 스택
- 큐
3. ***비선형 자료구조***
- 트리
- 그래프
4. 파일 자료구조
- 순차 파일
- 색인 파일
- 직접 파일

### 선형 자료구조

데이터를 한 줄로 순차적으로 표현한 형태. 선형 리스트, 연결 리스트, 스택, 큐 등

### 비선형 자료구조

하나의 데이터 뒤에 여러 개가 이어지는 형태. 트리와 그래프 등

## 알고리즘

어떤 문제를 해결해 가는 논리적인 과정

### 알고리즘 표현법

- 일반 언어 표현
- 순서도를 이용한 표현
- 의사코드를 이용한 표현
- 프로그램 코드로 표현

### 알고리즘의 성능

- 알고리즘 성능측정
알고리즘을 소요 시간을 기준으로 알고리즘 성능을 분석한 방법이 ‘시간 복잡도’
- 알고리즘 성능 표기
빅-오 표기법(Big-Oh Notation)으로 O(f(n))형태

---

# 2. 선형 리스트

## 선형 리스트의 기본

### 선형 리스트의 개념

- 데이터를 일정한 순서로 나열한 것
- 순차 리스트라고도 함
- 선형 리스트는 입력 순서대로 저장하는 데이터에 적당

## 선형리스트의 일반 구현

- 데이터 추가

```python
katok = []

def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')

print(katok)
```

- 데이터 삽입

```python
katok = ['다현', '정연', '쯔위', '사나', '지효', '모모']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

insert_data(3, '미나')
print(katok)
```

- 데이터 삭제

```python
katok = ['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None

    del katok[kLen-1]

delete_data(4)
print(katok)
```

- 전체 구현

```python
### 함수 선언부
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None

    del katok[kLen-1]

### 전역 변수부
katok=[]
select = -1

### 메인 코드부
while(select != 4):
    '''
    1: 추가, 2: 삽입, 3: 삭제, 4: 종료
    '''
    select = int(input("선택하세요 (1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
    if select not in (1,2,3,4):
        while select in (1,2,3,4):
            select = int(input("선택하세요 (1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

    if (select == 1):
        friend = input("추가할 데이터 --> ")
        add_data(friend)
        print(katok)

    elif (select == 2):
        position = int(input("삽입할 위치 --> "))
        friend = input("추가할 데이터 --> ")
        insert_data((position, friend))
        print(katok)

    elif (select == 3):
        position = int(input("삭제할 위치 --> "))
        delete_data((position))
        print(katok)

    elif (select == 4):
        print(katok)
        break
```

---

# 3. 단순 연결 리스트

## 단순 연결 리스트의 기본

방문할 맛집을 지도에 순서대로 연결한 것처럼, 떨어진 곳에 위치한 데이터를 화살표로 연결한 것

### 단순 연결 리스트의 개념

- 노드들이 물리적으로 떨어진 곳에 위치
- 각 노드의 번지도 순차적이지 않음
- 화살표로 표시된 연결(링크, Link)을 따라가면 선형 리스트 순서와 같음

### 단순 연결 리스트의 원리

- 노드 구조
- 노드(데이터) 삽입
- 노드(데이터) 삭제

## 단순 연결 리스트의 간단 구현

- 노드 생성과 연결

```python
### 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

### 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

print(node1.data, end='   ')
print(node1.link.data, end='   ')
print(node1.link.link.data, end='   ')
print(node1.link.link.link.data, end='   ')
print(node1.link.link.link.link.data, end='   ')
```

- 노드 삽입 삭제

```python
### 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

### 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# 삭제
node2.link = node3.link
del(node3)

## 삽입
# newNode = Node()
# newNode.data = '민중'
# newNode.link = node2.link
# node2.link = newNode

current = node1
print(current.data, end='   ')
while (current.link != None):
    current = current.link
    print(current.data, end='   ')
```

## 단순 연결 리스트의 일반 구현

- 단순 연결 리스트의 일반 형태

```python
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
```

- 노드 삽입, 삭제, 검색
    - 처음, 중간, 끝
    
    ```python
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
    ```
    
    ---
    

# 5. 원형 연결 리스트

## 원형 연결 리스트의 기본

시작 위치와 다음 위치가 계속 이어진 후 마지막에 다시 시작으로 돌아오는 형태

### 원형 연결 리스트의 개념

- 단순 연결 리스트와 구조와 구현 코드가 유사
- 리스트의 형태가 원(Circle) 형태로 구성(계속 회전하면서 연속 가능)
- 오버헤드가 발생하지 않음

---

# 6. 스택

## 스택의 기본

### 스택의 개념

- 스택(Stack) 자료구조는 한쪽 끝이 막힌 형태
- 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조

## 스택의 간단 구현

- 스택 생성,푸시,팝

```python
## 함수

## 전역
# stack = [ None, None, None, None, None ]
SIZE = 5    # 스택의 크기
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
# Push()
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥',stack)

# Pop()
data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝-->',data)

print('바닥',stack)
```

## 스택의 일반 구현

- 초기화, 데이터 삽입/추출/확인

```python
## 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print("스택이 꽉!")
        return
    else:
        top += 1
        stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택 텅!")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if isStackEmpty():
        print("스택 텅~")
        return None
    return stack[top]

## 전역
SIZE = 5    # 스택의 크기
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')

print(stack)

push('사이다')
print(stack)

retData = pop()
print('추출-->', retData)
retData = pop()
print('추출-->', retData)
retData = pop()
print('추출-->', retData)
print(stack)

print('다음 나올 데이터-->', peek())
```

- 스택 완성

```python
## 메인 코드 부분 ##
if __name__ == "__main__":
    select = input("삽입(I/추출(E)확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input('입력할 데이터 ==> ')
            push(data)
            print("스택 상태:",stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==>",data)
            print("스택 상태:",stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==>",data)
            print("스택 상태:",stack)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I/추출(E)확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")
```

---

# 7. 큐

## 큐의 기본

### 큐의 개념

- 큐(Queue) 자료 구조는 입구와 출구가 따로 있는 원통 형태

### 큐 원리

- 큐에 데이터를 삽입하는 작동: enQueue
- 데이터를 추출하는 작동: deQueue
- 저장된 데이터 중 첫 번째 데이터: front
- 저장된 데이터 중 마지막 데이터: rear

## 큐의 간단 구현

- 큐 생성, 데이터 삽입/추출

```python
## 함수

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인

# enQueue()
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print(f'출구 --<--  {queue}  --<-- 입구\n')

# deQueue()
front += 1
data = queue[front]
queue[front] = None
print(f'식사 손님: {data}')

front += 1
data = queue[front]
queue[front] = None
print(f'식사 손님: {data}')

front += 1
data = queue[front]
queue[front] = None
print(f'식사 손님: {data}\n')

print(f'출구 --<--  {queue}  --<-- 입구')
```

## 큐의 일반 구현

- 큐 초기화, 데이터 삽입/추출/확인

```python
## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE -1 and front == -1):
        return True
    else:
        for i in range(front+1, SIZE, 1):
            queue[i-1]  = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~~')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print(f'출구 --<--  {queue}  --<-- 입구')
# enQueue('민중')
# print(f'출구 --<--  {queue}  --<-- 입구')

retData = deQueue()
print('디큐 ==>', retData)
retData = deQueue()
print('디큐 ==>', retData)

print(f'출구 --<--  {queue}  --<-- 입구')

# print('다음 예정 손님 =>', peek())
# print(f'출구 --<--  {queue}  --<-- 입구')

enQueue('길동')
print(f'출구 --<--  {queue}  --<-- 입구')

enQueue('소희')
print(f'출구 --<--  {queue}  --<-- 입구')
```

## 큐의 응용

- 원형 큐

```python
## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~~')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~~')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미') # 원더걸스
print('출구<--', queue, '<--입구')

retData = deQueue()
print("디큐 ==> ", retData)
retData = deQueue()
print("디큐 ==> ", retData)
print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')

enQueue('소희')
print('출구<--', queue, '<--입구')
```

---

# 8. 이진 트리

## 이진 트리의 기본

### 이진 트리의 개념

- 트리(Tree) 자료구조는 나무를 거꾸로 뒤집어 놓은 형태
- 트리 자료구조 용어
    - 부모 노드, 자식 노드, 리프 노드, 루트, 에지, 차수

## 이진 탐색 트리의 구현

- 이진 탐색 트리의 생성

```python
## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역

## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode(); node4.data = '휘인'; node2.left = node4
node5 = TreeNode(); node5.data = '쯔위'; node2.right = node5
node6 = TreeNode(); node6.data = '선미'; node3.left = node6

print(node1.data)
print(node1.left.data,"\t",node1.right.data)
print(node1.left.left.data, "\t", node1.left.right.data, "\t", node1.right.left.data)
```

- 이진 탐색 트리 일반 구현/탐색

```python
## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
# 루트 노드 만들기
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:    # ['레드벨벳', '마마무', ... ]
    node = TreeNode()
    node.data = name

    current = root  # root 10이고, name이 6
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리 구성 완료!')

findData = '마마무'

current = root
while True:
    if findData == current.data:
        print(findData,"찾음")
        break
    elif findData < current.data:
        if current.left == None:
            print(findData,"없음")
            break
        current = current.left
    else:
        if current.right == None:
            print(findData, "없음")
            break
        current = current.right
```

# 그래프

## 그래프의 기본

### 그래프의 개념

- 여러 노드가 서로 연결된 구조
- 그래프 종류
    - 무방향 그래프
    - 방향 그래프
- 깊이 우선 탐색의 작동
    - 그래프의 모든 정점을 한 번씩 방문하는 것을 그래프 순회라고 함
    - 그래프 순회 방식은 깊이 우선 탐색, 너비 우선 탐색이 대표적
- 그래프의 인접 행렬 표현
    - 그래프를 코드로 구현할 때는 인접 행렬을 사용
    - 인접 행렬은 정방형으로 구성된 행렬로 정점이 4개인 그래프는 4X4로 표현