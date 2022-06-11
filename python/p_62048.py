# https://programmers.co.kr/learn/courses/30/lessons/62048
# 124 나라의 숫자

from math import *

def solution(w, h):
    answer = w * h
    sub = 0
    block = w

    if w < 2 or h < 2:
        answer = 0
    else:
        for i in range(w):
            if (h * i / w) - int((h * i / w)) == 0 and i != 0:
                block = i
                break;

            sub = sub + (ceil(h * (i + 1) / w) - floor(h * i / w))

    return int(answer - sub * (w // block))