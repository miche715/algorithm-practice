# https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 요격 시스템

def solution(targets):
    answer = 0
    target = sorted(targets, key=lambda x: (x[0], -x[1]))
    aim = target.pop(0)
    
    for target in target:
        if target[0] < aim[1] < target[1]:
            aim[0] = target[0]
        elif aim[0] <= target[0] and target[1] <= aim[1]:
            aim = target
        else:
            aim = target
            answer = answer + 1

    return answer + 1