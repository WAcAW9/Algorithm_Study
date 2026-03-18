# 플랫폼: 프로그래머스
# 번호: 120894
# 이름: 영어가 싫어요
# 난이도: level0
# 날짜: 2026-03-18
# 유형: 문자열 (replace)
# 노션: https://www.notion.so/327c3911b0a380abbea0c8348ea69dba

def solution(numbers):
    num_string=("zero","one","two","three","four","five","six","seven","eight","nine")

    for idx,s in enumerate(num_string):
        if s in numbers:
            numbers=numbers.replace(s,str(idx))

    return int(numbers)
