# https://programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

def solution(citations):
    n = []
    c = {}

    for i in range(len(citations)):
        n.append(int(citations[i]))
    n.sort(reverse = True)

    for i in range(len(n)):
       c[i + 1] = n[i]

    answer = len(c)
    for i in range(1, len(c) + 1):
        if i > c[i]:
            answer = i - 1
            break;

    return answer