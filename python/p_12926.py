# https://programmers.co.kr/learn/courses/30/lessons/12926
# 시저 암호

def solution(ss, n):
    answer = ''
    
    for s in ss:
        if s == " ":
            answer = answer + s
            continue
        if s.isupper():
            c = ord(s) + n
            if c > 90:
                c = 65 + c - 90 - 1
            answer = answer + chr(c)
        elif s.islower():
            c = ord(s) + n
            if c > 122:
                c = 97 + c - 122 - 1
            answer = answer + chr(c)
        
    return answer