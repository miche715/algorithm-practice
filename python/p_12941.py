# https://programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기

def solution(aa, bb):
    answer = 0
    aa.sort()
    bb.sort(reverse = True)
    
    for i in range(len(aa)):
        answer = answer + (aa[i] * bb[i])
    
    return answer