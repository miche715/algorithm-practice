# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기

def solution(arr):
    arr.remove(min(arr))
    
    if arr:
        return arr
    else:
        return [-1]