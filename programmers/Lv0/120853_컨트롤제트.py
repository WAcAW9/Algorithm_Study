# 플랫폼: 프로그래머스
# 번호: 120853
# 이름: 컨트롤 제트
# 난이도: level0
# 날짜: 2026-03-11
# 유형: 문자열 + 스택
# 노션: https://www.notion.so/320c3911b0a380dc972dfd6552cf9001

def solution(s):
    answer = 0
    temp=0
    for e in s.split():
        if e == "Z":
            answer-=temp
        else:
            answer+=int(e)
            temp=int(e)
    return answer
