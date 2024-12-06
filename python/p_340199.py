# https://school.programmers.co.kr/learn/courses/30/lessons/340199
# 지폐 접기

def solution(wallet, bill):
    count = 0
    
    while (wallet[0] < bill[0] or wallet[1] < bill[1]) and (wallet[0] < bill[1] or wallet[1] < bill[0]):
        if bill[0] >= bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
            
        count = count + 1
    
    return count