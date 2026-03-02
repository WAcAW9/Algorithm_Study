"""
문제: 프로그래머스 120837 개미 군단
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
노션: https://www.notion.so/30cc3911b0a38191b1e5eabf4d5c72a2
난이도: Level 0
분류: 그리디
날짜: 2026-02-12
핵심: 장군(5) → 병정(3) → 일개미(1) 순으로 큰 단위부터 탐욕적으로 배분
"""


def solution(hp):
    answer = 0
    # 장군 5 병정 3 일 1

    answer += (hp // 5)
    hp %= 5
    answer += (hp // 3)
    hp %= 3
    answer += int(hp)

    return answer
