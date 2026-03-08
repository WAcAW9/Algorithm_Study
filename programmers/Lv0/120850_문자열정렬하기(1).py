# 플랫폼: 프로그래머스
# 번호: 120850
# 이름: 문자열 정렬하기 (1)
# 난이도: level0
# 날짜: 2026-03-08
# 유형: 문자열 + 정렬 (숫자 추출)
# 노션: https://www.notion.so/1-31dc3911b0a3800b9196e877ed00d15b

def solution(my_string):
    answer = sorted([int(num) for num in my_string if num.isdigit()])
    return answer
