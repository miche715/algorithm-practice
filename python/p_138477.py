# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# 명예의 전당 (1)

def solution(k, score):
    hallOfFame = []
    answer = []
    
    for s in score:
        if not hallOfFame:
            hallOfFame.append([s])
        else:
            hallOfFame.append(hallOfFame[-1].copy())
            hallOfFame[-1].append(s)
            hallOfFame[-1] = sorted(hallOfFame[-1], reverse=True)[:k]
        answer.append(hallOfFame[-1][-1])
        
    return answer