# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr1[i] = format(arr1[i], "b")
        arr1[i] = ("0" * (n - len(arr1[i]))) + arr1[i]
        arr2[i] = format(arr2[i], "b")
        arr2[i] = ("0" * (n - len(arr2[i]))) + arr2[i]
        
        row = ""
        for j in range(len(arr1)):
            if int(arr1[i][j]) + int(arr2[i][j]) > 0:
                row = row + "#"
            else:
                row = row + " "
        answer.append(row)

    return answer