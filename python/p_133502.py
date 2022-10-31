# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 햄버거 만들기

def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(str(i))
        if len(stack) >= 4:
            if stack[-4] + stack[-3] + stack[-2] + stack[-1] == "1231":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer = answer + 1

    return answer