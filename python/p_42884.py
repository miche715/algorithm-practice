# https://programmers.co.kr/learn/courses/30/lessons/42884
# 단속 카메라

def solution(routes):
    answer = len(routes)
    stck = []
    
    routes = sorted(routes, key = lambda x: x[0])
    while routes:
        stck.append(routes.pop(0))
        while routes:
            r = routes.pop(0)
            flag = True
            for i in reversed(range(len(stck))):
                s = stck[i]
                if s[1] < r[0]:
                    flag = False
                    break
            if flag:
                stck.append(r)
                answer = answer - 1
            else:
                stck.clear()
                routes.insert(0, r)
                break
                      
    return answer