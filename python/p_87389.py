# https://programmers.co.kr/learn/courses/30/lessons/87389
# 나머지가 1이 되는 수 찾기

def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i