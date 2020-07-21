# [Do it! 실습 3C-1] seq_search() 함수를 사용하여 실수 검색하기
from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []  # 빈 리스트 x를 생성

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))  # 배열 마지막에 원소를 추가
    number += 1

ky = float(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력

idx = seq_search(x, ky)  # ky와 같은 값의 원소를 x에서 검색
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')