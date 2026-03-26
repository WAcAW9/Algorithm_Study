# 플랫폼: 프로그래머스
# 번호: 120907
# 이름: OX퀴즈
# 난이도: level0
# 날짜: 2026-03-26
# 유형: 문자열 (파싱)
# 노션: https://www.notion.so/OX-32fc3911b0a3802dad67ce3bb99edafe

def solution(quiz):
    answer = []
    for q in quiz:
        str_split = q.split()
        if str_split[1]=='+':
            if int(str_split[0])+int(str_split[2])==int(str_split[4]):
                answer.append("O")
            else : answer.append("X")
        else:
            if int(str_split[0])-int(str_split[2])==int(str_split[4]):
                answer.append("O")
            else : answer.append("X")
    return answer
