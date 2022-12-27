# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 가장 가까운 같은 글자

def solution(string):
    answer = []
    stack = []
    
    for s in string:
        if s in stack:
            answer.append(stack[::-1].index(s) + 1)
        else:
            answer.append(-1)
        stack.append(s)
                
    return answer