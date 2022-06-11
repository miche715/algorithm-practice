# https://programmers.co.kr/learn/courses/30/lessons/12985
# 예상 대진표

def solution(n, a, b):
    cnt = 0
    aa = min(a, b)
    bb = max(a, b)

    while True:
        cnt = cnt + 1
        if bb - aa == 1:
            if aa % 2 == 1 and bb % 2 == 0:
                return cnt
        if aa % 2 > 0:
            aa = (aa // 2) + 1
        else:
            aa = aa // 2
        if bb % 2 > 0:
            bb = (bb // 2) + 1
        else:
            bb = bb // 2