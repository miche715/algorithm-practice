# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기

def solution(number, k):
    digit = len(number) - k
    arr = []
    flag = False
    
    for i in range(len(number)):
        n = int(number[i])
        if arr:
            while arr[len(arr) - 1] < n:
                if len(arr) + len(number) - i == digit:
                    flag = True
                    break
                arr.pop()
                if not arr:
                    break
        if flag:
            arr.extend(number[i:])
            break
        arr.append(n)
    
    # while len(arr) > digit:
    #     arr.pop()
    
    return "".join(map(str, arr))