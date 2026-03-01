"""
문제: 프로그래머스 120834 외계 행성의 나이
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
노션: https://www.notion.so/30cc3911b0a381cdbc2cdecbdcc67a08
난이도: Level 0
분류: 문자열 처리
날짜: 2026-02-11
핵심: 숫자를 자릿수별로 분리하여 a~j 알파벳으로 변환 후 역순 조합
"""


def solution(age):

    alpha = 'abcdefghij'
    answer = ''

    while(age > 0):
        answer += alpha[age % 10]
        age //= 10

    return answer[::-1]
