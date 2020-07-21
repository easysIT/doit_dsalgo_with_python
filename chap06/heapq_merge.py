# 정렬을 마친 두 배열의 병합 (heapq.merege 사용）

import heapq

a = [2, 1, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))  # 배열 a와 b를 병합하여 c에 저장

print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
print(f'배열 a: {a}')
print(f'배열 b: {b}')
print(f'배열 c: {c}')