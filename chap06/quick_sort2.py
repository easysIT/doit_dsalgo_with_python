# [Do it! 실습 6-13] 퀵 정렬 알고리즘 구현하기(원소 수가 9개 미만인 경우 단순 삽입 정렬)

from typing import MutableSequence

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 가운데 값의 인덱스를 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 단순 삽입 정렬"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if right - left < 9:            # 원소 수가 9개 미만이면 단순 삽입 정렬을 호출
        insertion_sort(a, left, right)
    else:                           # 원소 수가 9개 이상이면 퀵 정렬을 수행
        pl = left                   # 왼쪽 커서
        pr = right                  # 오른쪽 커서
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 합니다(원소 수가 9개 미만이면 단순 삽입 정렬).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')