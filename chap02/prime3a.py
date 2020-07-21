# [Do it! 실습 2-10] 1,000 이하의 소수를 나열하기(알고리즘 개선 2) - 배열의 원솟수를 미리 결정하지 않음

counter = 0             # 곱셈과 나눗셈을 합한 횟수
prime = [2, 3]          # 소수를 저장하는 배열

for n in range(5, 1001, 2):     # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:   # 나누어 떨어지므로 소수가 아님
            break               # 반복 중단
        i += 1
    else:                       # 끝까지 나누어 떨어지지 않았다면
        prime += [n]            # 소수로 배열에 등록
        counter += 1

for i in prime:                 # 소수를 출력
    print(i)
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')