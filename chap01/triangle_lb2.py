# 왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기(언더스코어 사용)

print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.: '))

for i in range(n):          # 행 루프
    for _ in range(i + 1):  # 열 루프
        print('*', end='')
    print()