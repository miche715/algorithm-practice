# https://programmers.co.kr/learn/courses/30/lessons/72411
# 메뉴 리뉴얼

from itertools import *

def solution(orders, course):
    answer = []
    customer = {}
    com = {}
    temp = []

    for i in range(len((orders))):
        strstr = list(orders[i])
        strstr.sort()
        orders[i] = strstr

    for i in course:
        customer.clear()
        com.clear()
        temp.clear()
        max = 0
        for j in range(len(orders)):
            customer[j] = list(combinations(orders[j], i))
        for x in range(len(orders)):
            for y in range(len(customer[x])):
                setmenu = "".join(customer[x][y])
                if setmenu in com:
                    com[setmenu] = com[setmenu] + 1
                else:
                    com[setmenu] = 1
                if com[setmenu] > max and com[setmenu] > 1:
                    max = com[setmenu]
                    temp.clear()
                    temp.append(setmenu)
                elif com[setmenu] == max and com[setmenu] > 1:
                    temp.append(setmenu)
        for j in range(len(temp)):
            answer.append(temp[j])

    answer.sort()

    return answer