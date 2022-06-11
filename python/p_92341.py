# https://programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산

import math

def solution(fees, records):
    answer = []
    car = {}
    
    for r in records:
        c = r.split(" ")   
        if c[1] not in car.keys():
            car[c[1]] = []
        if c[2] == "IN":
            car[c[1]].insert(0, c[2])
            car[c[1]].append((int(c[0][:2]) * 60) + int(c[0][3:]))
        elif c[2] == "OUT":
            car[c[1]].pop(0)
            car[c[1]].append((int(c[0][:2]) * 60) + int(c[0][3:]) - car[c[1]].pop())
            
    for k in car.keys():
        if car[k][0] == "IN":
            car[k].pop(0)
            car[k].append((23 * 60) + 59 - car[k].pop())
        sum = 0
        for t in car[k]:
            sum = sum + t
        car[k] = sum
    car = sorted(car.items())
    
    for f in car:
        if f[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((f[1] - fees[0]) / fees[2])) * fees[3])

    return answer