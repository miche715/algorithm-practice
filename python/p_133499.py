# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 옹알이 (2)

def solution(babbling):
    answer = 0
    
    for b in babbling:
        stack = []
        if b.count("ayaaya") > 0 or b.count("yeye") > 0 or b.count("woowoo") > 0 or b.count("mama") > 0:
            continue
        for bs in b:
            stack.append(bs)
            if len(stack) == 2:
                if stack[0] + stack[1] == "ye" or stack[0] + stack[1] == "ma":
                    stack.pop()
                    stack.pop()
            if len(stack) == 3:
                if stack[0] + stack[1] + stack[2] == "aya" or stack[0] + stack[1] + stack[2] == "woo":
                    stack.pop()
                    stack.pop()
                    stack.pop()
            if len(stack) > 3:
                break
        if not stack:
            answer = answer + 1
        
    return answer