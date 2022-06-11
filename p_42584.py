# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격

def solution(prices):
    answer = []
    stck = []
    idx = []
    cnt = 0
    
    for i in range(len(prices) - 1):
        p = prices[i]
        cnt = cnt + 1
        answer.append(0)

        while True:
            if len(stck) == 0:
                stck.append(p)
                idx.append(i)
                break
            if stck[len(stck) - 1] > p:
                stck.pop()
                id = idx.pop()
                answer[id] = cnt - id - 1
            else:
                stck.append(p)
                idx.append(i)
                break
    for i in idx:
        answer[i] = cnt - i
    answer.append(0)
    
    return answer