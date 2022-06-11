# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) < 2:
            if scoville[0] < k:
                answer = -1
            break
        if scoville[0] < k:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer = answer + 1
        else:
            break

    return answer