# https://programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트

def solution(people, limit):
    answer = 0
    people = sorted(people)
    i = len(people) - 1
    j = 0
    
    while i > j:        
        if people[j] + people[i] <= limit:
            answer = answer + 1
            j = j + 1
        i = i - 1
    answer = answer + len(people) - (j * 2)
               
    return answer