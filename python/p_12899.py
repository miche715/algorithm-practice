# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

def solution(n):
    answer = ""
    quo = n
    convert = {0: "4", 1: "1", 2: "2"}

    while quo > 0:
        rem = quo % 3
        quo = quo // 3

        if rem == 0:
            quo = quo - 1

        answer = str(convert[rem]) + answer

    return answer