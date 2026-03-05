# 플랫폼: 프로그래머스
# 번호: 120847
# 이름: 최댓값 만들기(1)
# 난이도: level0
# 날짜: 2026-03-05
# 유형: 배열 (최댓값)
# 노션: https://www.notion.so/1-31ac3911b0a380f38f15e6d7e1fe8787

def solution(numbers):
    answer=0
    x=max(numbers)
    numbers.remove(x)
    y=max(numbers)
    answer=x*y
    return answer
