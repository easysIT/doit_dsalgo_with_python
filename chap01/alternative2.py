# [Do it! 실습 1-13] +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')  # n // 2개의 +-를 출력

if n % 2:
    print('+', end='')  # n이 홀수일 때만 +를 출력

print()