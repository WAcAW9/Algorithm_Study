"""
문제: 프로그래머스 120838 모스부호(1)
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120838
노션: https://www.notion.so/1-30cc3911b0a38117bc4af737a47fd52a
난이도: Level 0
분류: 해시맵(딕셔너리)
날짜: 2026-02-12
핵심: 모스부호 → 알파벳 딕셔너리 매핑 후 공백 기준 split하여 O(1) 조회
"""


def solution(letter):
    answer = ''
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    for l in letter.split():
        answer += morse.get(l, "")
    return answer
