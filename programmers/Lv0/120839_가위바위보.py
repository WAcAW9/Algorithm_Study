"""
문제: 프로그래머스 120839 가위 바위 보
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
노션: https://www.notion.so/30cc3911b0a3810fbb99dac2210dcf03
난이도: Level 0
분류: 해시맵(딕셔너리)
날짜: 2026-02-13
핵심: 가위(2)→바위(0), 바위(0)→보(5), 보(5)→가위(2) 승리 규칙을 딕셔너리로 매핑
"""


def solution(rsp):
    # 가위 2 바위 0 보 5
    # 바위 0 보 5 가위 2
    rule = {"2": "0", "0": "5", "5": "2"}
    answer = ''.join(rule[i] for i in rsp)

    return answer
