# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

def solution(s):
    s = list(s)
    start = 0
   
    for i in range(len(s)):
        if start == 0 and s[i].isalpha():
            s[i] = s[i].upper()
        elif s[i].isalpha():
            s[i] = s[i].lower()
        if s[i] == " ":
            start = 0
        else:
            start = start + 1

    return "".join(s)