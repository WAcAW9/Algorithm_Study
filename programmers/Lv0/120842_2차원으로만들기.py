# 플랫폼: 프로그래머스
# 번호: 120842
# 이름: 2차원으로 만들기
# 난이도: level0
# 날짜: 2026-02-27
# 유형: 구현 (리스트 슬라이싱)
# 노션: https://www.notion.so/2-314c3911b0a38059a304ed5bae40f310


def solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])

    return answer
