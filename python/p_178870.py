# https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 연속된 부분 수열의 합

import collections

def solution(sequence, k):
    answer = []
    index = collections.deque()
    sum = 0
    
    for i, s in enumerate(sequence):
        index.append(i)
        sum = sum + s
        
        while sum > k:
            sum = sum - sequence[index.popleft()]
            
        if sum == k:
            if not answer or (index[-1] - index[0] < answer[1] - answer[0]):
                answer = [index[0], index[-1]]

    return answer