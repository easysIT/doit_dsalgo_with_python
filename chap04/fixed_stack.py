# 고정 길이 스택 클래스 FixedStack 구현하기
# Do it! 실습 4-1 [A]
from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어 있는 FixedStack에 pop 또는 peek를 호출할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 push를 호출할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        self.ptr = 0                  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있는가?"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택은 가득 찼는가?"""
        return self.ptr >= self.capacity

# Do it! 실습 4-1 [B]
    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        if self.is_full():              # 스택이 가득 참
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
        if self.is_empty():             # 스택이 비어 있음
             raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """스택을 비움(모든 데이터를 삭제)"""
        self.ptr = 0

# Do it! 실습 4-1 [C]
    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 첨자(없으면 -1)를 반환"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1         # 검색 실패

    def count(self, value: Any) -> bool:
        """스택에 포함되어있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):  # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:
                c += 1             # 들어 있음
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 있는가?"""
        return self.count(value)

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])