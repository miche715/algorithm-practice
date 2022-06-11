# https://programmers.co.kr/learn/courses/30/lessons/42890
# 후보키

import itertools

def solution(relation):
    candi = []
    com = {}
    confirm = []
    
    for i in range(1, len(relation[0]) + 1):
        com[i] = list(map(set, itertools.combinations(range(len(relation[0])), i))) 
    
    for key in com.keys():
        for i in range(len(com[key])):
            flag = False
            for c in candi:
                if c.issubset(com[key][i]):
                    flag = True
                    break
            if flag:
                continue
            for j in range(len(relation)):
                tmp = ""
                for v in com[key][i]:
                    tmp = tmp + relation[j][v]
                if tmp not in confirm:
                    confirm.append(tmp)
            if len(confirm) == len(relation):
                candi.append(com[key][i])
            confirm.clear()

    if len(candi) > 0:
        answer = len(candi)
    else:
        answer = 1
        
    return answer