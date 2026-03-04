# 플랫폼: 프로그래머스
# 번호: 120845
# 이름: 주사위의 개수
# 난이도: level0
# 날짜: 2026-03-04
# 유형: 수학 (정수 나눗셈)
# 노션: https://www.notion.so/319c3911b0a3800a8319e1c7f587337b

def solution(box, n):
    answer = (box[0]//n) * (box[1]//n) * (box[2]//n)
    return answer
