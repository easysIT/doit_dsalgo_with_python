# [Do it! 실습 2-8] 1,000 이하의 소수를 나열하기

counter = 0  # 나눗셈 횟수

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0 :     # 나누어 떨어지면 소수가 아님
            break           # 반복은 더 이상 불필요하여 중단
    else:                   # 끝까지 나누어 떨어지지 않으면 다음을 수행
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')