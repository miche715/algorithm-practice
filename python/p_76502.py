# https://programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전하기

def solution(s):
    answer = 0
    arr = list(s)
    bracket = {")": "(", "}": "{", "]": "["}
    tmp = []
    
    for i in range(len(arr)):
        tmp.clear()
        for j in range(len(arr)):
            if arr[j] in bracket.keys():
                if len(tmp) > 0:
                    if bracket[arr[j]] == tmp[len(tmp) - 1]:
                        del tmp[len(tmp) - 1]
                    else:
                        break
                else:
                    tmp.append(arr[j])
                    break
            else:
                tmp.append(arr[j])
        if len(tmp) == 0:
            answer = answer + 1
        arr.append(arr.pop(0))
        
    return answer