# [Do it! 실습 6-4] 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2) - 정렬 과정을 출력

from typing import MutableSequence

def bubble_sort3_verbose(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    k = 0
    i = 0
    while k < n - 1:
        print(f'패스 {i + 1}')
        i += 1
        last = n - 1
        for j in range(n - 1, k, -1):
            for m in range(0, n - 1):
               print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                    ' +' if a[j - 1] > a[j] else ' -'),
                     end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        for m in range(0, n - 1):
           print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')

if __name__ == '__main__':
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort3_verbose(x)  # 배열 x를 버블

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')