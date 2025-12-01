# https://school.programmers.co.kr/learn/courses/30/lessons/451808
# 숫자 야구

from itertools import permutations

def make_strike_ball_list(result):
    return [int(r[0]) for r in result.split()]


def compare_strike_ball(a, b):
    a = str(a)
    b = str(b)

    strike = sum(a[i] == b[i] for i in range(4))
    ball = sum((digit in b) for digit in a) - strike

    return [strike, ball]


def filter_candinate(candidate, number, result):
    new_candinate = []
    for c in candidate:
        if compare_strike_ball(c, number) == result:
            new_candinate.append(c)

    return new_candinate


def solution(n, submit):
    answer = 1234
    candinate = [int(''.join(map(str, p))) for p in permutations(range(1, 10), 4)]

    for i in range(0, n):
        result = make_strike_ball_list(submit(answer))
        if result == [4, 0]: 
            return answer

        candinate = filter_candinate(candinate, answer, result)
        
        answer = candinate[0]

    return answer