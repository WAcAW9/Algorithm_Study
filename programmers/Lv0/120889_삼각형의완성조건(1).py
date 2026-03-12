# 플랫폼: 프로그래머스
# 번호: 120889
# 이름: 삼각형의 완성조건 (1)
# 난이도: level0
# 날짜: 2026-03-12
# 유형: 정렬 + 수학
# 노션: https://www.notion.so/1-321c3911b0a380fe850fec9b3f68e930

def solution(sides):
    x,y, max_len = sorted(sides)
    return 1 if (x+y)>max_len else 2
