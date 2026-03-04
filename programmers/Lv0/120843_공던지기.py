# 플랫폼: 프로그래머스
# 번호: 120843
# 이름: 공 던지기
# 난이도: level0
# 날짜: 2026-03-04
# 유형: 배열 (인덱스 조작)
# 노션: https://www.notion.so/319c3911b0a38064b095d51a6d7c802a

def solution(numbers, k):
    answer = 0
    for i in range(0,k*2,2):
        answer=numbers[i%len(numbers)]
    return answer
