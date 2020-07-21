# [Do it! 실습 6-17] 도수 정렬 알고리즘 구현하기

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):              f[a[i]] += 1                     # [1단계]
    for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2단계]
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3단계]
    for i in range(n):              a[i] = b[i]                      # [4단계]

def counting_sort(a: MutableSequence) -> None:
    """도수 정렬"""
    fsort(a, max(a))

if __name__ == '__main__':
    print('도수 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):  # 양수만 입력받음
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0: break

    counting_sort(x)  # 배열 x를 도수 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')