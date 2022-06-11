# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

def solution(priorities, location):
    paper = []
    cnt = 0

    for i in range(len(priorities)):
        paper.append(i)

    while True:
        flag = True
        for i in priorities:
            if priorities[0] < i:
                priorities.append(priorities[0])
                priorities.remove(priorities[0])
                paper.append(paper[0])
                paper.remove(paper[0])
                flag = False
                break
        if flag:
            priorities.pop(0)
            cnt = cnt + 1
            if paper.pop(0) == location:
                return cnt