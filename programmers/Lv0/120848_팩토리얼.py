# 플랫폼: 프로그래머스
# 번호: 120848
# 이름: 팩토리얼
# 난이도: level0
# 날짜: 2026-03-05
# 유형: 수학 (팩토리얼)
# 노션: https://www.notion.so/31ac3911b0a38088a246fd276fce44f1

from math import factorial
def solution(n):
    answer = 0
    for i in range(n):
        if(factorial(i)>n):
            answer=i-1
            break
    return answer
