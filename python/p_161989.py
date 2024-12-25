# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 덧칠하기

def solution(n, m, section):
    answer = 0
    stack = list()
    
    for s in reversed(section):
        if not stack:
            stack.append(s)
        else:
            if stack[0] - s + 1 <= m:
                stack.append(s)
            else:
                stack = [s]
                answer = answer + 1
    if stack:
        answer = answer + 1            
    
    return answer