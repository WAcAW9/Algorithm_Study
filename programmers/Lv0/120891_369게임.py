# 플랫폼: 프로그래머스
# 번호: 120891
# 이름: 369게임
# 난이도: level0
# 날짜: 2026-03-16
# 유형: 문자열
# 노션: https://www.notion.so/30cc3911b0a381f99734dbb9efd9841a

def solution(order):
    answer = 0
    clap ="369"
    for o in str(order) :
        for c in clap:
            if c==o : answer+=1
    return answer
