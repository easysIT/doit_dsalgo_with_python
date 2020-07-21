# [Do it! 실습 1-14] *를 n개 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))
w = int(input('몇 개마다 줄바꿈할까요? : '))

for i in range(n):      # n번 반복
    print('*', end='')
    if i % w == w - 1:  # n번 판단
        print()         # 줄바꿈

if n % w:
    print()             # 줄바꿈