# [Do it! 실습 5-3] 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정숫값을 입력하세요.: '))

recur(x)