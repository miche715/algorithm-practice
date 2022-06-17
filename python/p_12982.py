# https://programmers.co.kr/learn/courses/30/lessons/12982
# 예산

def solution(team, budget):
    answer = 0
    
    team.sort()
    for t in team:
        if(budget < t):
            break
        budget = budget - t
        answer = answer + 1
    
    return answer

print(solution([2,2,3,3], 10))