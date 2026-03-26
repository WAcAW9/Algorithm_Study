# 플랫폼: 프로그래머스
# 번호: 120902
# 이름: 문자열 계산하기
# 난이도: level0
# 날짜: 2026-03-26
# 유형: 문자열 (파싱)
# 노션: https://www.notion.so/32fc3911b0a380e59a0ae707ab0c8e7b

def solution(my_string):
    split_string = my_string.split()
    answer=int(split_string[0])
    for index,s in enumerate(split_string):
        if s=='+':
            answer+=int(split_string[index+1])
        if s=='-':
            answer-=int(split_string[index+1])

    return answer
