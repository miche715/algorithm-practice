# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    nlist = list(str(n))
    
    while nlist:
        answer.append(int(nlist.pop()))
        
    return answer