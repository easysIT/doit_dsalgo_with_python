# [Do it! 실습 3-2] for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key값이 같은 요소를 선형 검색(for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i  # 검색 성공(인덱스를 반환)
    return -1         # 검색 실패(-1을 반환)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))  # num 값을 입력
    x = [None] * num                           # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력받음

    idx = seq_search(x, ky)                     # ky와 값이 같은 요소를 x에서 검색

    if idx == -1:
        print('검색 값을 갖는 요소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')