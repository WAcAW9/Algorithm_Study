# 플랫폼: 프로그래머스
# 번호: 120895
# 이름: 인덱스 바꾸기
# 난이도: level0
# 날짜: 2026-03-20
# 유형: 문자열
# 노션: https://www.notion.so/327c3911b0a380ac9940c9a6dbf31ec1

def solution(my_string, num1, num2):

    return my_string[:num1] + my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:]
