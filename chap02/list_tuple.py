# 리스트와 튜플 생성

list01 = []                 # [] 빈 리스트 생성
list02 = [1, 2, 3]          # [1, 2, 3]
list03 = ['A', 'B', 'C', ]  # ['A', 'B', 'C'] 맨 마지막 원소에 쉼표를 써도 됨

list04 = list()           # [] 빈 리스트 생성
list05 = list('ABC')      # ['A', 'B', 'C'] 각각의 문자로부터 원소 생성
list06 = list([1, 2, 3])  # [1, 2, 3] 리스트로부터 원소 생성
list07 = list((1, 2, 3))  # [1, 2, 3] 튜플로부터 원소 생성
list08 = list({1, 2, 3})  # [1, 2, 3] 집합으로부터 원소 생성

list09 = list(range(7))         # [0, 1, 2, 3, 4, 5, 6]
list10 = list(range(3, 8))      # [3, 4, 5, 6, 7]
list11 = list(range(3, 13, 2))  # [3, 5, 7, 9, 11]

# 원소 수가 5이고 모든 원소값이 없는 리스트를 생성
list12 = [None] * 5  # [None, None, None, None, None]

tuple01 = ()              # ()
tuple02 = 1,              # (1,)
tuple03 = (1,)            # (1,)
tuple04 = 1, 2, 3         # (1, 2, 3)
tuple05 = 1, 2, 3,        # (1, 2, 3)
tuple06 = (1, 2, 3)       # (1, 2, 3)
tuple07 = (1, 2, 3, )     # (1, 2, 3)
tuple08 = 'A', 'B', 'C',  # ('A', 'B', 'C')

tuple09 = tuple()           # () 빈 튜플 생성
tuple10 = tuple('ABC')      # ('A', 'B', 'C') 문자열의 각 문자로부터 원소를 생성
tuple11 = tuple([1, 2, 3])  # (1, 2, 3) 리스트로부터 원소 생성
tuple12 = tuple({1, 2, 3})  # (1, 2, 3) 집합으로부터 원소 생성

tuple13 = tuple(range(7))         # (0, 1, 2, 3, 4, 5, 6)
tuple14 = tuple(range(3, 8))      # (3, 4, 5, 6, 7)
tuple15 = tuple(range(3, 13, 2))  # (3, 5, 7, 9, 11)

print('list01 =', list01)
print('list02 =', list02)
print('list03 =', list03)
print('list04 =', list04)
print('list05 =', list05)
print('list06 =', list06)
print('list07 =', list07)
print('list08 =', list08)
print('list09 =', list09)
print('list10 =', list10)
print('list11 =', list11)
print('list12 =', list12)

print('tupe01 =', tuple01)
print('tupe02 =', tuple02)
print('tupe03 =', tuple03)
print('tupe04 =', tuple04)
print('tupe05 =', tuple05)
print('tupe06 =', tuple06)
print('tupe07 =', tuple07)
print('tupe08 =', tuple08)
print('tupe09 =', tuple09)
print('tupe10 =', tuple10)
print('tupe11 =', tuple11)
print('tupe12 =', tuple12)
print('tupe13 =', tuple13)
print('tupe14 =', tuple14)
print('tupe15 =', tuple15)