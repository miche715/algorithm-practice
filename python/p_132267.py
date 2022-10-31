# https://school.programmers.co.kr/learn/courses/30/lessons/132267
# 콜라 문제

def solution(a, b, coke):
    answer = 0
    
    while coke >= a:
        temp = coke // a
        answer = answer + (temp * b)
        coke = (temp * b) + (coke % a)
            
    return answer