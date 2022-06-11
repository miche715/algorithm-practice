# https://programmers.co.kr/learn/courses/30/lessons/12953
# N개의 최소공배수

def solution(arr):
    answer = 0
    arr.sort()
    n = arr[-1]
    
    while answer == 0:
        flag = True
        for a in arr:
            if n % a != 0:
                flag = False
                break
        if flag:
            answer = n
            break
        n = n + 1
    
    return answer