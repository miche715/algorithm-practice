# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

def solution(length, limit, truck):
    bridge = [0 for i in range(length)]
    time = 0
    w = 0

    while True:
        time = time + 1
        w = w - bridge.pop()
        bridge.insert(0, 0)
        if truck:
            if w + truck[0] <= limit:
                bridge[0] = truck.pop(0)
        w = w + bridge[0]
        if len(truck) == 0 and w == 0:
            break
            
    return time