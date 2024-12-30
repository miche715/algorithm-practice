# https://school.programmers.co.kr/learn/courses/30/lessons/340211
# 충돌위험 찾기

def solution(points, routes):
    answer = 0
    
    point = {}
    for i, p in enumerate(points, 1):
        point[i] = p
    
    path = []
    for route in routes:
        temp1 = []
        temp2 = []
        for i in range(len(route)):
            if i + 1 == len(route):
                break
            start_point = point[route[i]]
            end_point = point[route[i + 1]]
            if start_point[0] <= end_point[0]:
                for y in range(start_point[0], end_point[0] + 1):
                    if len(temp2) > 0 and temp2[-1] == [y, start_point[1]]:
                        continue
                    temp2.append([y, start_point[1]])
            else:
                for y in reversed(range(end_point[0], start_point[0] + 1)):
                    if len(temp2) > 0 and temp2[-1] == [y, start_point[1]]:
                        continue
                    temp2.append([y, start_point[1]])
            if start_point[1] <= end_point[1]:
                for x in range(start_point[1], end_point[1] + 1):
                    if len(temp2) > 0 and temp2[-1] == [temp2[-1][0], x]:
                        continue
                    temp2.append([temp2[-1][0], x])
            else:
                for x in reversed(range(end_point[1], start_point[1] + 1)):
                    if len(temp2) > 0 and temp2[-1] == [temp2[-1][0], x]:
                        continue
                    temp2.append([temp2[-1][0], x])
            temp1.extend(temp2)
        path.append(temp2)
    
    move = {}
    crash = {}
    for pa in path:
        for i, p in enumerate(pa):
            if i not in move.keys():
                move[i] = [p]
            else:
                if p in move[i]:
                    if i not in crash.keys():
                        crash[i] = [p]
                        answer = answer + 1
                    elif p not in crash[i]:
                        crash[i].append(p)
                        answer = answer + 1
                else:
                    move[i].append(p)

    return answer