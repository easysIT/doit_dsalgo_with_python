# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)

from stack import Stack  # stack.py의 Stack 클래스를 임포트

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n 값을 푸시
            n = n - 1
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정수값을 입력하세요.: '))

recur(x)