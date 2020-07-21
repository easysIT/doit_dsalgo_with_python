 # [Do it! 실습 1-23] 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변 길이를 입력하세요.: '))

for i in range(n):              # 행 루프
    for _ in range(n - i - 1):  # 열 루프(공백을 출력)
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')      # 열 루프(*을 출력)
    print()