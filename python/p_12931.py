# https://programmers.co.kr/learn/courses/30/lessons/12931
# 자릿수 더하기

def solution(n):
    answer = 0

    for s in str(n):
        answer = answer + int(s)

    return answer