# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

import math

def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            answer = answer + 1
    
    return answer