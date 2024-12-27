# https://school.programmers.co.kr/learn/courses/30/lessons/340212
# 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    min_level = 0
    max_level = 100000

    while True:
        cur_level = (min_level + max_level) // 2
        time = 0
        for i in range(len(diffs)):
            if i == 0:
                time = time + times[i]
            else:
                fail = 0
                if diffs[i] > cur_level:
                    fail = diffs[i] - cur_level
                time = time + ((times[i - 1] + times[i]) * fail) + times[i]
                if time > limit:
                    if min_level == cur_level:
                        min_level = cur_level + 1
                    else:
                        min_level = cur_level
                    break
        else:
            if min_level == max_level or min_level + 1 == max_level or time == limit:
                if cur_level == 0:
                    return 1
                else:
                    return cur_level
            else:
                max_level = cur_level