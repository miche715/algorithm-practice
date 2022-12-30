# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 기사단원의 무기

import math

def solution(number, limit, power):
    level = []
    answer = 0
    
    for num in range(1, number + 1):
        div = 0
        
        for n in range(1, int(math.sqrt(num)) + 1):
            if n ** 2 == num:
                div = div + 1
            elif num % n  == 0:
                div = div + 2
        level.append(div)
    
    for i in range(len(level)):
        if level[i] > limit:
            level[i] = power
    
    return sum(level)