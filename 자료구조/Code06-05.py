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