# 플랫폼: 프로그래머스
# 번호: 120892
# 이름: 암호 해독
# 난이도: level0
# 날짜: 2026-03-16
# 유형: 문자열
# 노션: https://www.notion.so/325c3911b0a380b1a919f0951cd26c10

def solution(cipher, code):
    return cipher[code-1::code]
