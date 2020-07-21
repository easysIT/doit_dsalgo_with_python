# [Do it! 실습 5-4] 재귀 함수의 구현(꼬리 재귀를 제거)

def recur(n: int) -> int:
    """꼬리 재귀를 제거한 함수 recur"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2
x = int(input('정수값을 입력하세요.: '))

recur(x)