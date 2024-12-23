# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# 공원 산책

def solution(park, routes):
    position = []
    
    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == "S":
                position = [y, x]
                break
        else:
            continue
        break
        
    for r in routes:
        direction, distance = r.split(" ")
        distance = int(distance)

        if direction == "E":
            for x in range(position[1], position[1] + distance + 1):
                if position[1] + distance >= len(park[position[0]]) or park[position[0]][x] == "X":
                    break
            else:
                position = [position[0], position[1] + distance]     
        if direction == "W":
            for x in range(position[1] - distance, position[1] + 1):
                if position[1] - distance < 0 or park[position[0]][x] == "X":
                    break
            else:
                position = [position[0], position[1] - distance]
        if direction == "S":
            for y in range(position[0], position[0] + distance + 1):
                if position[0] + distance >= len(park) or park[y][position[1]] == "X":
                    break
            else:
                position = [position[0] + distance, position[1]]
        if direction == "N":
            for y in range(position[0] - distance, position[0] + 1):
                if position[0] - distance < 0 or park[y][position[1]] == "X":
                    break
            else:
                position = [position[0] - distance, position[1]]
        
    return position