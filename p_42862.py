# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복

def solution(n, lost, reserve):
    no = lost.copy()
    
    for l in lost:
        if l in reserve:
            no.remove(l)
            reserve.remove(l)
    
    answer = n - len(no)
    
    for n in no:
        if n - 1 in reserve:
            reserve.remove(n - 1)
            answer = answer + 1
        elif n + 1 in reserve:
            reserve.remove(n + 1)
            answer = answer + 1
    
    return answer