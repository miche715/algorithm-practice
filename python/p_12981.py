# https://programmers.co.kr/learn/courses/30/lessons/12981
# 영어 끝말잇기

def solution(n, words):
    answer = []
    use = []
    
    for i in range(len(words)):
        w = words[i]
        if w not in use:
            if i > 0:
                u = use[len(use) - 1]
                if u[len(u) - 1] != w[0]:
                    answer.append((i % n) + 1)
                    answer.append((i // n) + 1)
                    break
            use.append(words[i])
        else:
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break
    if not answer:
        answer.append(0)
        answer.append(0)
    
    return answer