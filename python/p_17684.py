# https://programmers.co.kr/learn/courses/30/lessons/17684
# 압축

def solution(msg):
    answer = []
    dic = {}
    
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    
    i = 0
    while i < len(msg):
        m = msg[i]
        j = 1
        while m in dic.keys():
            if i + j == len(msg):
                m = m + " "
                break
            m = m + msg[i + j]
            j = j + 1
        dic[m] = len(dic) + 1
        answer.append(dic[m[:-1]])
        i = i + len(m[:-1])
    
    return answer