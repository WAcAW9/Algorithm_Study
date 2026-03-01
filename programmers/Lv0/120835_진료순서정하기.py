"""
문제: 프로그래머스 120835 진료순서 정하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
노션: https://www.notion.so/30cc3911b0a381ba9912cb68d55efbf9
난이도: Level 0
분류: 정렬
날짜: 2026-02-11
핵심: 내림차순 정렬 후 각 원소의 순위(인덱스+1)를 반환
"""


def solution(emergency):
    answer = []

    temp = sorted(emergency, reverse=True)

    for e in emergency:
        for t in temp:
            if(e == t):
                answer.append(temp.index(t) + 1)

    return answer
