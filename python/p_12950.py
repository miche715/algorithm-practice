# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    li = []
    
    for i in range(len(arr1)):
        li.clear()
        for j in range(len(arr1[i])):
            li.append(arr1[i][j] + arr2[i][j])
        answer.append(li.copy())
    
    return answer