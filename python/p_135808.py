# https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=python3
# 과일 장수

def solution(k, m, score):
    box = []
    answer = 0
    
    score.sort()
    while True:
        box.append(score.pop())
        if len(box) == m:
            answer = answer + min(box) * m
            box.clear()
        if not score:
            break
    
    return answer