# https://programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    for a in arr:
        if not answer:
            answer.append(a)
        else:
            if not answer[len(answer) - 1] == a:
                answer.append(a)

    return answer

print(solution([1,1,3,3,0,1,1]))