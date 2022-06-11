# https://programmers.co.kr/learn/courses/30/lessons/12980
# 점프와 순간 이동

def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 != 0:
            n = n - 1
            ans = ans + 1
        n = n // 2

    return ans