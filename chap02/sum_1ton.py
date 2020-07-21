# [Do it! 실습 2C-5] 1부터 n까지 정수의 합 구하기

def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지 합은 {sum_1ton(x)}입니다.')