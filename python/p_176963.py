# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 추억 점수

def solution(name, yearning, photo):
    answer = []
    score = {name[i]: yearning[i] for i in range(len(name))}
    
    for pt in photo:
        sum = 0
        
        for p in pt:
            if p in score.keys():
                sum = sum + score[p]
                
        answer.append(sum)
    
    return answer