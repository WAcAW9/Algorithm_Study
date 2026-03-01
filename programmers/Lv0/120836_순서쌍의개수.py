"""
문제: 프로그래머스 120836 순서쌍의 개수
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
노션: https://www.notion.so/30cc3911b0a381a4b1cce03bd4cd5af0
난이도: Level 0
분류: 수학 (약수)
날짜: 2026-02-11
핵심: 1~n 순회하며 n의 약수 개수를 카운트 → 순서쌍의 수와 동일
"""


def solution(n):
    answer = 0
    for i in range(n):
        if(n % (i + 1) == 0):
            answer += 1

    return answer
