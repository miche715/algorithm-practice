# https://school.programmers.co.kr/learn/courses/30/lessons/181187
# 두 점 사이의 정수 쌍

from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 0
    
    for r in range(1, r2 + 1):
        if r < r1:
            answer = answer + (floor(sqrt(r2 ** 2 - r ** 2)) - ceil(sqrt(r1 ** 2 - r ** 2)) + 1)
        else:
            answer  = answer + (floor(sqrt(r2 ** 2 - r ** 2)) + 1)
            
    return answer * 4