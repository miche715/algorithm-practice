# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

def solution(ss):
    answer = ''
    i = 0
    
    for s in ss:
        if s == " ":
            answer = answer + " "
            i = 0
            continue
        if i % 2 == 0:
            answer = answer + s.upper()
        else:
            answer = answer + s.lower()
        i = i + 1
        
    return answer