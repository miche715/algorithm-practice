# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# 과제 진행하기

def solution(plans):
    answer = []
    plan_stack = []
    
    for plan in sorted(plans, key=lambda x: x[1]):
        plan[1] = sum(int(t) * 60 ** i for i, t in enumerate(reversed(plan[1].split(":"))))
        plan[2] = int(plan[2])        
        if plan_stack:
            duration = plan[1] - plan_stack[-1][1]
            while plan_stack:
                if plan_stack[-1][2] - duration <= 0:
                    duration = duration - plan_stack[-1][2]
                    answer.append(plan_stack.pop()[0])
                else:
                    plan_stack[-1][1] = plan[1]
                    plan_stack[-1][2] = plan_stack[-1][2] - duration
                    break
        plan_stack.append(plan)
    for plan in reversed(plan_stack):
        answer.append(plan[0])
        
    return answer