# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 문자열 나누기

def solution(string):
    answer = 0
    
    while string:
        targrt = string[0]
        num = [0, 0]
        flag = False
        for i in range(len(string)):
            if string[i] == targrt:
                num[0] = num[0] + 1
            else:
                num[1] = num[1] + 1
            if num[0] == num[1]:
                string = string[i + 1:]
                flag = True
                break
        if not flag:
            string = ""
        answer = answer + 1
            
    return answer