# 플랫폼: 프로그래머스
# 번호: 120844
# 이름: 배열 회전시키기
# 난이도: level0
# 날짜: 2026-03-04
# 유형: 자료구조 (덱)
# 노션: https://www.notion.so/319c3911b0a3808cbf77e66151781cee

from collections import deque
def solution(numbers, direction):
    d = deque(numbers)
    d.rotate(1 if direction == "right" else -1)
    answer = list(d)

    return answer
