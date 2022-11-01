# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 숫자 짝꿍

def solution(x, y):
    answer = ''
    digit = []
    
    for i in reversed(range(10)):
        digit.append(min(x.count(str(i)), y.count(str(i))))
    i = 9
    for d in digit:
        if i == 0 and answer == "" and d > 0:
            answer = "0"
            break
        answer = answer + str(i) * d
        i = i - 1
    if answer == "":
        answer = "-1"
    
    return answer