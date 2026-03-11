# 플랫폼: 프로그래머스
# 번호: 120852
# 이름: 소인수분해
# 난이도: level0
# 날짜: 2026-03-11
# 유형: 수학 (소인수분해)
# 노션: https://www.notion.so/320c3911b0a38098b485f020c0d87f68

def solution(n):
    answer = []

    for i in range(2,n+1):
        if (n%i==0):
            answer.append(i)
            while (n%i==0):
                n//=i
    return answer
