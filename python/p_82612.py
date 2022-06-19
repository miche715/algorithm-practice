# https://programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기

def solution(price, money, count):
    sum = 0

    for i in range(1, count + 1):
        sum = sum + (price * i)
    
    if money >= sum:
        return 0
    else:
        return sum - money