# 플랫폼: 프로그래머스
# 번호: 120890
# 이름: 가까운 수
# 난이도: level0
# 날짜: 2026-03-13
# 유형: 정렬 + 탐색
# 노션: https://www.notion.so/321c3911b0a3808c8535dd5b4f371202

def solution(array, n):
    min_sub = float('INF')
    for item in sorted(array):
        if min_sub > abs(item-n):
            answer = item
            min_sub = abs(item-n)
    return answer
