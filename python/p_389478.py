# https://school.programmers.co.kr/learn/courses/30/lessons/389478
# 택배 상자 꺼내기

def solution(n, w, num):
    answer = 0
    box = [
        ([i * w + j + 1 if i * w + j + 1 <= n else -1 for j in range(w)][::-1] 
        if i % 2 == 1 
        else 
        [i * w + j + 1 if i * w + j + 1 <= n else -1 for j in range(w)])
        for i in range((n + w - 1) // w)
    ]
    target_x = -1

    for y in box:
        for i, x in enumerate(y):
            if x == num:
                target_x = i
            if target_x == i and x > -1:
                answer = answer + 1

    return answer