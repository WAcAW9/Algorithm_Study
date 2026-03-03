# 플랫폼: 프로그래머스
# 번호: 120840
# 이름: 구슬을 나누는 경우의 수
# 난이도: level0
# 날짜: 2026-02-13
# 유형: 수학 (조합론)
# 노션: https://www.notion.so/30cc3911b0a38179b857e71e9ba04c8d


def factorial(n):
    if n <= 1: return 1
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))
