# https://programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐

import heapq

def solution(operations):
    arr = []
    
    for o in operations:
        oper = o.split(" ")
        
        if oper[0] == "I":
            heapq.heappush(arr, int(oper[1]))
        elif oper[0] == "D":
            if not arr:
                continue
            else:
                if oper[1] == "1":
                    arr.pop()
                elif oper[1] == "-1":
                    heapq.heappop(arr)
    
    if arr:
        return [max(arr), min(arr)]
    else:
        return [0, 0]