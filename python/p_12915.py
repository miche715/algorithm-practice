# https://programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))