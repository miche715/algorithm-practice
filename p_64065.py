# https://programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    answer = []
    arr = []
    ary = []
    num = ""

    for i in range(len(s)):
        if 48 <= ord(s[i]) <= 57:
            num = num + s[i]
        elif s[i] == "," and num != "":
            ary.append(int(num))
            num = ""
        elif s[i] == "}" and (len(ary) > 0 or num != ""):
            ary.append(int(num))
            num = ""
            arr.append(list(ary))
            ary.clear()
    arr = sorted(arr, key = lambda x: len(x))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in answer:
                answer.append(arr[i][j])
                break

    return answer