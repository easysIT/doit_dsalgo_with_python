# [Do it! 실습 1-17] 가로 세로가 정수이고 넓이가 area인 직사각형에서 변의 길이를 나열하기

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):  # 1부터 사각형의 넓이 계산
    if i * i > area: break
    if area % i: continue
    print(f'{i} × {area // i}')