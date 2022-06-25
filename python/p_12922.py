# https://programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수박수박수?

def solution(n):
    answer = ""
    watermelon = ["수", "박"]
    
    for i in range(n):
        answer = answer + watermelon[i % 2]
    
    return answer