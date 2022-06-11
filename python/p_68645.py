# https://programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이

def solution(n):
    answer = []
    arr = []
    cnt = 0
    pos = "d"
    
    if n == 1:
        return [1]
    
    for i in range(n):
        arr.append([])
        for j in range(i + 1):
            arr[i].append(0)
            
    i = 0
    j = 0
    while cnt != (n * (n + 1)) / 2:
        cnt = cnt + 1
        arr[i][j] = cnt
        if pos == "d":
            i = i + 1
            if i + 1 == len(arr):
                pos = "r"
            elif arr[i + 1][j] != 0:
                pos = "r"    
        elif pos == "r":
            j = j + 1
            if j + 1 == len(arr[i]):
                pos = "ul"
            elif arr[i][j + 1] != 0:
                pos = "ul"  
        elif pos == "ul":
            i = i - 1
            j = j - 1
            if arr[i - 1][j - 1] != 0:
                pos = "d"
    
    for a in arr:
        answer.extend(a)
        
    return answer