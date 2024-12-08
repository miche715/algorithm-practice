# https://school.programmers.co.kr/learn/courses/30/lessons/250137
# 붕대 감기

def solution(bandage, health, attacks):
    current_health = health
    current_attack = [0, 0]
    count = 0
    
    for i in range(1, attacks[-1][0] + 1):        
        if i == attacks[0][0]:
            current_attack = attacks.pop(0)
            current_health = current_health - current_attack[1]
            count = 0
            if current_health <= 0:
                return -1
        else:
            current_health = current_health + bandage[1]
            count = count + 1
            if count == bandage[0]:
                current_health = current_health + bandage[2]
                count = 0
            if current_health > health:
                current_health = health
    
    return current_health