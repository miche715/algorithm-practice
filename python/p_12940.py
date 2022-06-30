# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최소공배수

def getGCD(n, m):  # 최대공약수
    while m != 0:
        a = n % m
        n = m
        m = a
    
    return n


def getLCM(n, m):  # 최소공배수
    i = 2
    a = n

    while a % m != 0:
        a = n * i
        i = i + 1
    
    return a


def solution(n, m):
    return [getGCD(max(n, m), min(n, m)), getLCM(max(n, m), min(n, m))]