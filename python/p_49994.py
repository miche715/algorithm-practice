# https://programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

def solution(dirs):
    answer = 0
    pos = [0, 0]
    road = set()
    
    for d in dirs:
        x = pos[0]
        y = pos[1]
        
        if d == "U":
            pos[1] = pos[1] + 1
            if pos[1] > 5:
                pos[1] = 5
            else:
                road.add(((x, pos[1]), (x, y)))
        if d == "D":
            pos[1] = pos[1] - 1
            if pos[1] < -5:
                pos[1] = -5
            else:
                road.add(((x, y), (x, pos[1])))
        if d == "R":
            pos[0] = pos[0] + 1
            if pos[0] > 5:
                pos[0] = 5
            else:
                road.add(((pos[0], y), (x, y)))
        if d == "L":
            pos[0] = pos[0] - 1
            if pos[0] < -5:
                pos[0] = -5
            else:
                road.add(((x, y), (pos[0], y)))

    answer = len(road)
    
    return answer