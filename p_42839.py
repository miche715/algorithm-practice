# https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

from itertools import *
from math import *

def solution(numbers):
    per = {}
    num = []
    prime = []

    for i in range(len(numbers)):
        per[i] = list(permutations(numbers, i + 1))

    for i in range(len(per)):
        for j in range(len(per[i])):
            tmp = int("".join(per[i][j]))
            if num.count(tmp) == 0:
                if tmp > 1:
                    num.append(tmp)
                    prime.append(tmp)

    for i in range(len(num)):
        for j in range(2, int(sqrt(num[i])) + 1):
            if num[i] % j == 0:
                prime.remove(num[i])
                break

    return len(prime)