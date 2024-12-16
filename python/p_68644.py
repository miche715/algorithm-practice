# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

import itertools

def solution(numbers):
    answer = set()
    com = tuple(itertools.combinations(numbers, 2))
    
    for c in com:
        answer.add(c[0] + c[1])
    
    return sorted(list(answer))