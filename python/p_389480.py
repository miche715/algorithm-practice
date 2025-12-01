# https://school.programmers.co.kr/learn/courses/30/lessons/389480
# 완전범죄

def solution(info, n, m):
    info = sorted(info, key = lambda x: (-(x[0] / x[1]), -x[0], x[1]))
    sum = [0, 0]
    answer = 0

    for i in info:
        if i[1] + sum[1] < m:
            sum[1] = sum[1] + i[1]
        else:
            sum[0] = sum[0] + i[0]

    answer = sum[0]
    if answer >= n:
        answer = -1

    return answer