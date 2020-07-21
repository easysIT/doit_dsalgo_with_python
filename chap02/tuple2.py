# 튜플의 모든 원소를 ​​enumerate 함수로 스캔하기

x = ('John', 'George', 'Paul', 'Ringo')

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')