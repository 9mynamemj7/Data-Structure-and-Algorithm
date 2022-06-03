# 알고리즘

# 11. 정렬 기본

## 정렬의 개념

- 순서대로 데이터가 나열되어 있는 것

### 정렬 알고리즘의 종류

- 선택 정렬
    - 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬
- 삽입 정렬
    - 기존 데이터 중에서 자신의 위치를 찾아 데이터를 삽입하는 정렬
- 버블 정렬
    - 
- 퀵 정렬

## 기본 정렬 알고리즘의 원리와 구현

- 선택정렬

```python
import random
## 함수
def findMinIndex(ary):  # ary에서 제일 작은 위치를 찾기
    minIndex = 0
    for i in range(1, len(ary)):
        if (ary[minIndex] > ary[i]):
            minIndex = i
    return minIndex

## 전역
before = [random.randint(1, 100) for _ in range(20)]
after = []

## 메인
print('정렬 전 -->', before)
for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬 후 -->', after)
```

```python
import random
## 함수
def selctionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) : # Cycle
        minIndex = i
        for k in range(i+1, n) :
            if (ary[minIndex] > ary[k]) :
                minIndex = k

        ary[i], ary[minIndex] = ary[minIndex], ary[i]

    return ary

## 변수
dataAry = [random.randint(1, 100) for _ in range(8)]

## 메인
print('정렬 전 -->', dataAry)
dataAry = selctionSort(dataAry) # sorted(배열)
print('정렬 후 -->', dataAry)
```

# 13. 검색

## 검색의 기본

### 검색 알고리즘의 종류

- 순차 검색
    - 검색할 집합이 정렬 되어 있지 않은 상태일 때
    - 처음부터 차례대로 찾아보는 것으로, 쉽지만 비효율적임
    - 집합의 데이터가 정렬되어 있지 않다면 이 검색 외에 특별한 방법 없음
- **이진 검색**
    - 데이터가 정렬되어 있다면 이진 검색도 사용 가능
    - 순차 검색에 비해 월등히 효율적이라 데이터가 몇 천만 개 이상이어도 빠르게 찾아낼 수 있음
- 트리 검색
    - 데이터 검색에는 상당히 효율적이지만 트리의 삽입, 삭제 등에는 부담

## 순차 검색과 이진 검색 알고리즘의 원리와 구현

```python
## 함수
def binarySearch(ary, fData):
    pos = -1

    start = 0
    end = len(ary) -1

    while (start <= end):
        mid = (start + end) // 2
        if ary[mid] == fData:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

    return pos

## 전역
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162  # 할머니 키

## 메인
print('배열-->',dataAry)
position = binarySearch(dataAry, findData)
if position == -1:
    print(findData, '가 없음...')
else:
    print(f'{findData}가 {position}위치에 있음')
```

# 10. 재귀

## 재귀 호출의 기본

### 재귀호출의 개념

- 재귀 호출(Recursion)은 자신을 다시 호출하는 것

### 재귀 호출의 작동

```python
## 함수
def openBox():
    global count
    print('상자를 엽니다')
    count -= 1
    if count == 0:
        print('** 선물은 넣기.... ***')
        return

    openBox()
    print('상자를 닫습니다')

## 메인
count = 10
openBox()
```

```python
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))
```

![Untitled](%E1%84%8B%E1%85%A1%E1%86%AF%E1%84%80%E1%85%A9%E1%84%85%E1%85%B5%E1%84%8C%E1%85%B3%E1%86%B7%20663c85235b8e4402803319e51eb9af45/Untitled.png)