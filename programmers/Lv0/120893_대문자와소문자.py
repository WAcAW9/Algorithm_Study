# 플랫폼: 프로그래머스
# 번호: 120893
# 이름: 대문자와 소문자
# 난이도: level0
# 날짜: 2026-03-16
# 유형: 문자열
# 노션: https://www.notion.so/325c3911b0a380489823ddf1fa17129c#325c3911b0a38190a160caba894cebab

def solution(my_string):
    answer = ''
    for s in my_string :
        if s.isupper():
            answer+=s.lower()
        else : answer+=s.upper()
    return answer
