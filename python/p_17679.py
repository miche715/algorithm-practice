# https://programmers.co.kr/learn/courses/30/lessons/17679
# 프렌즈4블록

def solution(m, n, board):
    answer = 0
    arr = []
    erase = set()
    score = m * n + 1
    
    for b in board:
        arr.append(list(b))
    
    while score > 0:
        erase.clear()
        for i in range(m - 1):
            for j in range(n - 1):
                if arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1] and arr[i][j] != "-":
                    erase.add((i, j))
                    erase.add((i + 1, j))
                    erase.add((i, j + 1))
                    erase.add((i + 1, j + 1))
        if score == 0:
            break
        score = len(erase)
        answer = answer + score
        for e in erase:
            arr[e[0]][e[1]] = "-"
        for x in range(n):
            y = 0
            tmp = ""
            while y < m - 1:
                if arr[y][x].isalpha() and arr[y + 1][x] == "-":
                    tmp = arr[y + 1][x]
                    arr[y + 1][x] = arr[y][x]
                    arr[y][x] = tmp
                    y = 0
                else:
                    y = y + 1
    
    return answer