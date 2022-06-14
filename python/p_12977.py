# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

import itertools
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    sum = 0

    com = list(itertools.combinations(nums, 3))
    
    for co in com:
        for c in co:
            sum = sum + c
        if(isPrime(sum)):
            answer = answer + 1
        sum = 0

    return answer