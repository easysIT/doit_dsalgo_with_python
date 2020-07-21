# recur 함수를 거꾸로 출력(Do it! 실습 5-3 수정)

def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현(거꾸로 출력)"""
    if n > 0:
        recur(n - 2)
        print(n)
        recur(n - 1)

x = int(input('정숫값을 입력하세요.: '))

recur(x)