# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 가장 많이 받은 서물

def solution(friends, gifts):
    answer = {}
    giftGrid = {}
    giftIndex = {}
    
    for me in friends:
        answer[me] = 0
        giftGrid[me] = {}
        giftIndex[me] = 0
        for friend in friends:
            if me != friend:
                giftGrid[me][friend] = 0
        
    for gift in gifts:
        me = gift.split(" ")[0]
        friend = gift.split(" ")[1]
        giftGrid[me][friend] = giftGrid[me][friend] + 1
        giftIndex[me] = giftIndex[me] + 1
        giftIndex[friend] = giftIndex[friend] - 1
    
    for me, grid in giftGrid.items():
        for friend in grid.keys():
            if grid[friend] > giftGrid[friend][me]:
                answer[me] = answer[me] + 1
            elif grid[friend] == giftGrid[friend][me] and giftIndex[me] > giftIndex[friend]:
                answer[me] = answer[me] + 1
    
    return max(answer.values())