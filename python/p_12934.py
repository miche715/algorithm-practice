# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별

import math

def solution(n):
    if math.sqrt(n) % 1 == 0:
        return (math.sqrt(n) + 1) ** 2
    else:
        return -1