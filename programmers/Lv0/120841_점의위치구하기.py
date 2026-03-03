# 플랫폼: 프로그래머스
# 번호: 120841
# 이름: 점의 위치 구하기
# 난이도: level0
# 날짜: 2026-02-27
# 유형: 수학 (사분면)
# 노션: https://www.notion.so/314c3911b0a38080a0d2ff2fb7d8a118


def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        return 4
    if dot[1] < 0:
        return 3
    return 2
