# https://programmers.co.kr/learn/courses/30/lessons/42860
# 조이스틱

def curMove(tmp, cur, move, flag):
    cur1 = cur
    cur2 = cur
    move1 = 0
    move2 = 0
    
    if flag == 0:
        if tmp[cur] == 'A':
            while tmp[cur1] == 'A':
                cur1 = cur1 + 1
                move1 = move1 + 1
            while tmp[cur2] == 'A':
                cur2 = cur2 - 1
                move2 = move2 + 1
            if move1 < move2:
                cur = cur1
                move = move1
            else:
                cur = cur2
                move = move2
    elif flag == 1:
        if tmp[cur] == 'A':
            while tmp[cur1] == 'A':
                cur1 = cur1 + 1
                move1 = move1 + 1
            cur = cur1
            move = move1
    elif flag == 2:
        if tmp[cur] == 'A':
            while tmp[cur2] == 'A':
                cur2 = cur2 + 1
                move2 = move2 + 1
            cur = cur2
            move = move2
    
    return cur, move


def solution(name):
    answer = [0, 0]
    alphabet = {}
    
    for i in range(0, 14):
        alphabet[chr(65 + i)] = i
    for i in range(14, 26):
        alphabet[chr(65 + i)] = 26 - i
    
    name = list(name)
    tmp = name.copy()
    cur = 0
    move = 0
    start = False
    while len(tmp) != tmp.count('A'):
        if start:     
            cur, move = curMove(tmp, cur, move, 0)
        else:
            cur, move = curMove(tmp, cur, move, 1)
            start = True
        answer[0] = answer[0] + alphabet[tmp[cur]] + move
        move = 0
        tmp[cur] = 'A'
    
    tmp = name.copy()
    cur = 0
    move = 0
    start = False
    while len(tmp) != tmp.count('A'):
        if start:     
            cur, move = curMove(tmp, cur, move, 0)
        else:
            cur, move = curMove(tmp, cur, move, 2)
            start = True
        answer[1] = answer[1] + alphabet[tmp[cur]] + move
        move = 0
        tmp[cur] = 'A'
           
    return min(answer[0], answer[1])