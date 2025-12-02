# https://school.programmers.co.kr/learn/courses/30/lessons/389479
# 서버 증설 횟수

import math

def solution(players, m, k):
    answer = 0
    capacity = m
    expire = {}

    for i, p in enumerate(players):
        if i in expire.keys():
            capacity = capacity - (expire[i] * m)

        increase = 0
        if p - capacity >= 0:
            increase = math.ceil((p - capacity) / m)
            if increase == 0 or (p - capacity) % m == 0:
                increase = increase + 1
        
        if increase > 0:
            capacity = capacity + (increase * m)
            expire[i + k] = increase
        answer = answer + increase

    return answer