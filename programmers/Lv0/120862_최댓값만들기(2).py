# 플랫폼: 프로그래머스
# 번호: 120862
# 이름: 최댓값 만들기 (2)
# 난이도: level0
# 날짜: 2026-03-26
# 유형: 정렬
# 노션: https://www.notion.so/2-32fc3911b0a3803ead92d4b7dd5a9ec9

def solution(numbers):
    copy_numbers = sorted(numbers[:])

    return max(copy_numbers[0]*copy_numbers[1],copy_numbers[len(numbers)-1]*copy_numbers[len(numbers)-2])
