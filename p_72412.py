# https://programmers.co.kr/learn/courses/30/lessons/72412
# 순위 검색

from itertools import *
from bisect import *

def solution(info, query):
    answer = []
    qq = []
    qd = {}
    kindof = [["java", "python", "cpp", "-"], ["backend", "frontend", "-"], ["junior", "senior", "-"], ["pizza", "chicken", "-"]]

    temp = list(map("".join, product(*kindof)))
    for i in temp:
        qd[i] = [-1]
    for i in range(len(info)):
        parc = info[i].split(" ")
        tmp = list(map("".join, product(*[[parc[0], "-"], [parc[1], "-"], [parc[2], "-"], [parc[3], "-"]])))
        for j in tmp:
            qd[j].append(int(parc[4]))
    for i in qd:
        qd[i].sort()

    for i in range(len(query)):
        qq.append(query[i].split(" and "))
        tmp = qq[i].pop(3).split(" ")
        qq[i].append(tmp[0])
        qq[i].append(tmp[1])
        key = qq[i][0] + qq[i][1] + qq[i][2] + qq[i][3]
        value = qd[key]
        score = int(qq[i][4])
        cnt = (len(value) - 1) - (bisect_left(value, score) - 1)
        answer.append(cnt)

    return answer