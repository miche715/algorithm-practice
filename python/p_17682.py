# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임

def solution(dartResult):
    ll = []
    answer = ["0"]
    oper = {"S": "**1", "D": "**2", "T": "**3", "*": "*2", "#": "*(-1)"}
    
    for i in range(len(dartResult)):
        if dartResult[i] in oper.keys():
            if dartResult[i] == "*" and len(ll) > 2:
                ll.insert(len(ll) - 2, oper[dartResult[i]])
            ll.append(oper[dartResult[i]])
        else:
            ll.append(dartResult[i])
    
    for l in ll:
        if len(l) == 1:
            if len(answer[len(answer) - 1]) == 1 and len(answer) > 1:
                answer[len(answer) - 1] = answer[len(answer) - 1] + l
            else:
                answer.append("+")
                answer.append(l)
        else:
            answer.append(l)
    
    return eval("".join(answer))