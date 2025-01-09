# https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 도넛과 막대 그래프

def solution(edges):
    start = 0
    donut = 0
    stick = 0
    eight = 0
    gragh = {}
    
    for edge in edges:
        if edge[0] not in gragh.keys():
            gragh[edge[0]] = [[edge[1]], []]
        else: 
            gragh[edge[0]][0].append(edge[1])
        if edge[1] not in gragh.keys():
            gragh[edge[1]] = [[], [edge[0]]]
        else: 
            gragh[edge[1]][1].append(edge[0])
            
        if len(gragh[edge[0]][0]) >= 2 and len(gragh[edge[0]][1]) == 0:
            start = edge[0]

    for node in gragh[start][0]:
        if start in gragh[node][0]:
            gragh[node][0].remove(start)
        if start in gragh[node][1]:
            gragh[node][1].remove(start)
        
        current_node = node
        while True:
            current_gragh = gragh[current_node]
            if len(current_gragh[0]) == 2:
                eight = eight + 1
                break
            elif len(current_gragh[0]) == 0 or len(current_gragh[1]) == 0:
                stick = stick + 1
                break
            elif gragh[current_node][0][0] == node:
                donut = donut + 1
                break

            current_node = current_gragh[0][0]
    
    return [start, donut, stick, eight]