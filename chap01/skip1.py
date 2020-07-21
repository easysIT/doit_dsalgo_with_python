# [Do it! 실습 1-19] 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
    
print()