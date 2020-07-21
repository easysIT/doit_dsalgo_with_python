 # [Do it! 실습 1C-4] 함수의 내부·외부에서 정의한 변수와 객체의 식별 번호를 출력

n = 1      # 전역 변수(함수 내부·외부에서 사용)
def put_id():
    x = 1  # 지역 변수(함수 내부에서만 사용)
    print(f'id(x) = {id(x)}')
    
print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()