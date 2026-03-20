# 플랫폼: 프로그래머스
# 번호: 120896
# 이름: 한 번만 등장한 문자
# 난이도: level0
# 날짜: 2026-03-20
# 유형: 문자열
# 노션: https://www.notion.so/329c3911b0a380f8a721d1c5d422e9c2

from collections import Counter
def solution(s):
    return ''.join(sorted(num for num,count in Counter(s).items() if count==1))
