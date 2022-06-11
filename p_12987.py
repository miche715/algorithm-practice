# https://programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임

def solution(ta, tb):
    answer = 0
    ta.sort(reverse = True)
    tb.sort(reverse = True)
    i = 0
    j = 0
    
    while i < len(ta):
        if tb[j] > ta[i]:
            answer = answer + 1
            i = i + 1
            j = j + 1
        else:
            i = i + 1
        
    return answer