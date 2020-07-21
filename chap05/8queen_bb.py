# [Do it! 실습 5-8] 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8       # 각 열에서 퀸의 위치
flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크

def put() -> None:
    """각 열에 놓은 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if not flag[j]:  # j 행에 퀸을 배치하지 않았으면
            pos[i] = j   # 퀸을 j 행에 배치
            if i == 7:   # 모든 열에 퀸을 배치를 완료
                put()
            else:
                flag[j] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag[j] = False

set(0)  # 0열에 퀸을 배치