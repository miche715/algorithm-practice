# https://programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    strings = sorted(strings, key = lambda x: x[n])
    
    print(strings)
    
    
    return answer

solution(["sun", "bed", "car"], 1)