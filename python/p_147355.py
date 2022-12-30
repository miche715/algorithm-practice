# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 크기가 작은 부분문자열

def solution(t, p):
    subStrings = []
    length = len(p)
    i = 0
    
    while length + i <= len(t):
        subStrings.append(int(t[i:length + i]))
        i = i + 1

    return len(list(filter(lambda s: s <= int(p), subStrings)))