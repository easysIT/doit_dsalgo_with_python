# 이진 검색 알고리즘(검색에 실패할 때 ValueError를 내보냄）

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 요소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 요소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 요소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 요소의 인덱스
        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    raise ValueError  # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    print('오름차순으로 입력하세요.')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('검색할 값을 입력하세요.: '))  # 키 ky를 입력받음

    try:
        idx = bin_search(x, ky)                 # ky와 같은 값의 요소를 x에서 검색
    except ValueError:
        print('검색값을 갖는 요소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')