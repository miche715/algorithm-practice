# https://programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수

import operator

def solution(numbers):
    strnum = dict()
    digit = dict()
    answer = ""

    for i in range(len(numbers)):
        digit[i] = len(str(numbers[i]))
        strnum[i] = str(numbers[i]) * 3
    snum = sorted(strnum.items(), key = operator.itemgetter(1), reverse = True)

    for i in range(len(snum)):
        answer = answer + snum[i][1][0:digit[snum[i][0]]]

    if int(answer) == 0:
        answer = str(0)

    return answer