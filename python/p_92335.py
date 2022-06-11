# https://programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기

import math

def solution(n, k):
    answer = 0
    num = ""
    cnt = 0
    
    while n > 0:
        rem = n % k
        n = n // k
        num = num + str(rem)
    num = num[::-1].split("0")
    
    for n in num:
        if not n or n == "1":
            continue
        n = int(n)
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                cnt = cnt + 1
                break
        if cnt == 0:
            answer = answer + 1
        cnt = 0
    
    return answer