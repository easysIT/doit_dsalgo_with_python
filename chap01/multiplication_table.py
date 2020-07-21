# [Do it! 실습 1-21] 구구단 곱셈표 출력하기

print('-' * 27)
for i in range(1, 10):      # 행 루프
    for j in range(1, 10):  # 열 루프
        print(f'{i * j : 3}', end='')
    print()                 # 행 변경
print('-' * 27)