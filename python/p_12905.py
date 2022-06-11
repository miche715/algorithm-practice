# https://programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기

def isAllZero(board):
    for b in board:
        if 1 in b:
            return False
    return True

def solution(board):
    arr = board.copy()
    length = 1

    if isAllZero(board):
        return 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            arr[i][j] = min(min(arr[i][j - 1], arr[i - 1][j]), arr[i - 1][j - 1]) + 1
            length = max(length, arr[i][j])
            
    return length ** 2