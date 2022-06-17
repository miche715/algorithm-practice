# https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        for b in board:
            if b[m - 1] != 0:
                if stack:
                    if stack[len(stack) - 1] != b[m - 1]:
                        stack.append(b[m - 1])
                    else:
                        stack.pop()
                        answer = answer + 2
                else:
                    stack.append(b[m - 1])
                b[m - 1] = 0
                break
    
    return answer