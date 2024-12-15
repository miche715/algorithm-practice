# https://school.programmers.co.kr/learn/courses/30/lessons/250125
# 이웃한 칸

def solution(board, h, w):
    count = 0
    near = []
    
    if w + 1 < len(board[h]):
        near.append([h, w + 1])
    if w - 1 >= 0:
        near.append([h, w - 1])
    if h + 1 < len(board):
        near.append([h + 1, w])
    if h - 1 >= 0:
        near.append([h - 1, w])
        
    for n in near:
        if board[n[0]][n[1]] == board[h][w]:
            count = count + 1
        
    return count