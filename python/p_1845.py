# https://programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬

def solution(nums):
    ponketmon = set(nums)
    
    if len(ponketmon) <= len(nums) // 2:
        return len(ponketmon)
    else:
        return len(nums) // 2