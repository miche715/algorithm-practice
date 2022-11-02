# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기

def solution(survey, choices):
    answer = ""
    score = {
        "R": 0, "T": 0, 
        "C": 0, "F": 0, 
        "J": 0, "M": 0, 
        "A": 0, "N": 0, 
        }
    
    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] = score[survey[i][0]] + abs(choices[i] - 4)
        if choices[i] > 4:
            score[survey[i][1]] = score[survey[i][1]] + abs(choices[i] - 4)
    keys = list(score.keys())
    for i in range(0, len(keys), 2):
        if score[keys[i]] >= score[keys[i + 1]]:
            answer = answer + keys[i]
        else:
            answer = answer + keys[i + 1]
    
    return answer