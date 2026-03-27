# 플랫폼: 프로그래머스
# 번호: 120861
# 이름: 캐릭터의 좌표
# 난이도: level0
# 날짜: 2026-03-27
# 유형: 시뮬레이션
# 노션: https://www.notion.so/32fc3911b0a3806ebf4fd6aee06f42f9

def solution(keyinput, board):
    dx,dy=0,0

    for keyin in keyinput:
        if keyin=="right"and board_range(dx+1,dy,board):
            dx+=1
            continue
        elif keyin=="left"and board_range(dx-1,dy,board):
            dx-=1
            continue
        elif keyin=="up"and board_range(dx,dy+1,board):
            dy+=1
            continue
        elif keyin=="down"and board_range(dx,dy-1,board):
            dy-=1
            continue

    return [dx,dy]

def board_range(dx, dy, board):
    board_x, board_y = board
    return abs(board_x//2)>=abs(dx) and abs(board_y//2)>=abs(dy)
