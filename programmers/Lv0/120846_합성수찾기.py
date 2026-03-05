# 플랫폼: 프로그래머스
# 번호: 120846
# 이름: 합성수 찾기
# 난이도: level0
# 날짜: 2026-03-05
# 유형: 수학 (합성수 판별)
# 노션: https://www.notion.so/31ac3911b0a380b6aeb4e62646e8353b

def solution(n):
    answer = 0
    for i in range(n+1):
        for j in range(2,i):
            if(i%j==0):
                answer+=1
                break

    return answer
