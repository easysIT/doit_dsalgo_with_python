# [Do it! 실습 2C-3] 리스트의 모든 요소를 ​​enumerate 함수로 스캔(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')