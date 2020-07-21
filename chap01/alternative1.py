# [Do it! 실습 1-12] +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):          # 반복 n번
    if i % 2:                 
        print('-', end='')  # 홀수인 경우 - 출력
    else:
        print('+', end='')  # 짝수인 경우 + 출력

print()