def solution(n):
    answer = ""
    watermelon = ["수", "박"]
    
    for i in range(n):
        answer = answer + watermelon[i % 2]
    
    return answer