# https://programmers.co.kr/learn/courses/30/lessons/12978
# 배달

def solution(n, road, time):
    answer = 0
    path = [[500001 for i in range(n)] for j in range(n)]
    
    for r in road:
        path[r[0] - 1][r[1] - 1] = min(path[r[0] - 1][r[1] - 1], r[2])
        path[r[1] - 1][r[0] - 1] = min(path[r[1] - 1][r[0] - 1], r[2])
        path[r[0] - 1][r[0] - 1] = 0
        path[r[1] - 1][r[1] - 1] = 0
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                path[j][k] = min(path[j][k], path[i][k] + path[j][i])

    for t in path[0]:
        if t <= time:
            answer = answer + 1
            
    return answer