# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측

def solution(num):
    for i in range(1, 500):
        if num == 1:
            return 0
        if num % 2 == 0:
            num= num // 2
        else:
            num = (num * 3) + 1
        if num == 1:
            return i
    
    return -1