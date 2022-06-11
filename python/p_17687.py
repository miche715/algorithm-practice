# https://programmers.co.kr/learn/courses/30/lessons/17687
# n진수 게임

def solution(n, t, m, p):
    answer = ''
    nota = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    game = ""
    
    for i in range(t * m):
        num = i
        tmp = ""
        while num > 0:
            rem = num % n
            if rem in nota.keys():
                rem = nota[rem]
            tmp = tmp + str(rem)
            num = num // n
        if not tmp:
            tmp = "0"
        game = game + tmp[::-1]
    
    for i in range(len(game)):
        if i % m == p - 1:
            answer = answer + game[i]
        if len(answer) == t:
            break 
        
    return answer