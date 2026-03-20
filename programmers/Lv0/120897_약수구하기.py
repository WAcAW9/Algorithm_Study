# 플랫폼: 프로그래머스
# 번호: 120897
# 이름: 약수 구하기
# 난이도: level0
# 날짜: 2026-03-20
# 유형: 수학
# 노션: https://www.notion.so/1-329c3911b0a3806093dbea5c4a8fb8df

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i==0: answer.append(i)

    return answer
