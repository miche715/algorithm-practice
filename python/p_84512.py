# https://programmers.co.kr/learn/courses/30/lessons/84512
# 모음 사전

import itertools

def solution(word):
    answer = 0
    dic = []
    vowel = ["A", "E", "I", "O", "U"]
    
    for i in range(1, 6):
        dic.extend(list(map("".join, itertools.product(vowel, repeat = i))))
    dic.sort()
    
    return dic.index(word) + 1