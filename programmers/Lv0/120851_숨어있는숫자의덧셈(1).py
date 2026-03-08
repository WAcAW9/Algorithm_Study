# 플랫폼: 프로그래머스
# 번호: 120851
# 이름: 숨어있는 숫자의 덧셈 (1)
# 난이도: level0
# 날짜: 2026-03-08
# 유형: 문자열 (숫자 추출 + 합산)
# 노션: https://www.notion.so/1-31dc3911b0a380369122faf11867748a

def solution(my_string):
    answer = sum([int(num) for num in my_string if num.isdigit()])
    return answer
