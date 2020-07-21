# 병합 정렬 알고리즘 구현하기(heapq.merge를 사용)

from typing import MutableSequence
import heapq

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬(heapq.merge를 사용)"""
    atype = type(a)

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left]～a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 앞부분 배열의 병합 정렬
            _merge_sort(a, center + 1, right)       # 뒷부분 배열의 병합 정렬

            buff = atype(heapq.merge(a[left: center+1], a[center + 1: right+1]))
            for i in range(len(buff)):
                a[left + i] = buff[i]

    _merge_sort(a, 0, len(a))       # 배열 전체를 병합 정렬

if __name__ == '__main__':
    print('병합 정렬을 수행합니다(heapq.merge를 사용).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')