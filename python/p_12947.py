# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수

def solution(x):
    if x % sum(map(int, list(str(x)))) == 0:
        return True
    else:
        return False