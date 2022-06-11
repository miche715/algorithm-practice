# https://programmers.co.kr/learn/courses/30/lessons/87946
# 피로도

import itertools as itertool

def solution(k, dungeons):
    answer = []
    per = list(itertool.permutations(range(len(dungeons)), len(dungeons)))
    
    for p in per:
        tmp = k
        clear = 0
        for t in p:
            if tmp >= dungeons[t][0]:
                tmp = tmp - dungeons[t][1]
                clear = clear + 1
            else:
                break
        answer.append(clear)
    answer.sort(reverse = True)
    
    return answer[0]