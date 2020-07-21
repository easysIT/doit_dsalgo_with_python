# [Do it! 실습 5-6] 하노이의 탑 구현하기

def move(no: int, x: int, y: int) -> None:
    """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('하노이의 탑을 구현하는 프로그램입니다.')
n = int(input('원반의 개수를 입력하세요.: '))

move(n, 1, 3)