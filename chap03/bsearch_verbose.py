# [Do it! 실습 3C-3] 이진 검색 알고리즘의 실행 과정을 출력

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)"""
    pl = 0           # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 원소의 인덱스

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스

        print('   |', end='')
        if pl != pc:         # pl 원소 위에 <-를 출력
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else: 
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:         # pr 원소 위에 ->를 출력
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='') 
        print('\n   |')

        if a[pc] == key:
            return pc    # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:  
            break
    return -1            # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                 break

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 ky를 입력

    idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')