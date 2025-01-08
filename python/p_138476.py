# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 귤 고르기

from collections import Counter

def solution(k, tangerine):
    answer = 0
    in_box = 0

    for _, v in Counter(tangerine).most_common():
        in_box = in_box + v
        answer = answer + 1
        if in_box >= k:
            break

    return answer