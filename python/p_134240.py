# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 푸드 파이트 대회

def solution(food):
    answer = ""
    
    for i in range(len(food)):
        if i == 0:
            continue
        answer = answer + str(i) * (food[i] // 2)
    answer = answer + "0" + answer[::-1]
    
    return answer