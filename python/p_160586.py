# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 대충 만든 자판

def solution(keymap, targets):
    answer = []
    key_hash = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in key_hash.keys() or key_hash[keymap[i][j]] >= j + 1:
                key_hash[keymap[i][j]] = j + 1
    
    for tar in targets:
        sum = 0
        for t in tar:
            if t not in key_hash.keys():
                answer.append(-1)
                break
            else:
                sum = sum + key_hash[t]
        else:
            answer.append(sum)
    
    return answer