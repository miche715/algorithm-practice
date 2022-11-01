# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 삼총사

import itertools

def solution(number):
    return list(map(sum, itertools.combinations(number, 3))).count(0)