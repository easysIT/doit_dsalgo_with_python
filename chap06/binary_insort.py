# [Do it! 실습 6C-2] 이진 삽입 정렬 알고리즘의 구현(bisect.insort 사용)

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬(bisect.insort을 사용)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)

if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num            # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)    # 배열 x를 이진 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')