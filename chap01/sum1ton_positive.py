# [Do it! 실습 1-16] 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:
        break  # n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i  # sum에 i를 더함
    i += 1    # i에 1을 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')