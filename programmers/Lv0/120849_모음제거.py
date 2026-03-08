# 플랫폼: 프로그래머스
# 번호: 120849
# 이름: 모음 제거
# 난이도: level0
# 날짜: 2026-03-08
# 유형: 문자열 (replace)
# 노션: https://www.notion.so/31dc3911b0a380e6b876e42936fc3711

def solution(my_string):
    answer = my_string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

    return answer
