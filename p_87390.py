# https://programmers.co.kr/learn/courses/30/lessons/87390
# n^2 배열 자르기

def solution(n, left, right):
    answer = []
    cnt = left
    
    for i in range(left, right + 1):
        row = cnt // n
        col = cnt % n
        if col < row + 1:
            col = row
        answer.append(col + 1)
        cnt = cnt + 1
        
    return answer