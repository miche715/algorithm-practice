# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문자열 내 p와 y의 개수

def solution(ss):
    sl = []
    
    for s in ss:
        sl.append(s.lower())
    
    return sl.count("p") == sl.count("y")