# [보충수업 5-1] 양의 정수인 팩토리얼 구하기(n이 음수면 ValueError 예외 처리 발생)

def factorial(n : int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함(n이 음수면 ValueError 예외 처리 발생)"""
    if n > 0:
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    else:
        raise ValueError

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    try:
        print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
    except ValueError:
        print(f'{n}의 팩토리얼은 구할 수 없습니다.')