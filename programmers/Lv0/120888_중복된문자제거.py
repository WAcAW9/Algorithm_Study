# 플랫폼: 프로그래머스
# 번호: 120888
# 이름: 중복된 문자 제거
# 난이도: level0
# 날짜: 2026-03-12
# 유형: 문자열
# 노션: https://www.notion.so/321c3911b0a380469455e229e5064c1b

def solution(my_string):
    li = []
    answer = ''
    for s in my_string :
        if s in li : continue
        else :
            li.append(s)
            answer+=s
    return answer
