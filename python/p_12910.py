# https://programmers.co.kr/learn/courses/30/lessons/12910
# 나누어 떨어지는 숫자 배열

def solution(arr, div):
    answer = []
    
    arr.sort()
    for a in arr:
        if a % div == 0:
            answer.append(a)
            
    if not answer:
        answer.append(-1)
    
    return answer