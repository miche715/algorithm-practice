# https://programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

def solution(n):
    answer = 0
    onec = format(n, "b").count("1")
    
    while answer == 0:
        n = n + 1
        if format(n, "b").count("1") == onec:
            answer = n
        
    return answer