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




