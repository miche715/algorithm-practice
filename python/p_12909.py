# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

def solution(bracket):
    stk = []
    
    for b in bracket:
        if b == "(":
            stk.append(b)
        else:
            if stk:
                if stk[len(stk) - 1] == "(":
                    stk.pop()
                else:
                    break
            else:
                stk.append(b)
                break
    
    if stk:
        return False
    else:
        return True