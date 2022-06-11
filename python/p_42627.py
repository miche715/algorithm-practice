# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

def solution(jobs):
    time = 0  # 처리한 jobs[i][1]들의 합
    tsum = 0  # 처리 시간의 합
    sjobs = sorted(jobs, key = lambda x: (x[0], x[1]))
    task = []

    while len(sjobs) > 0:
        task.clear()
        for i in range(len(sjobs)):
            if sjobs[i][0] <= time:
                task.append(sjobs[i])
            else:
                break
        if len(task) > 0:
            task = sorted(task, key = lambda x: x[1])
            tsum = tsum + time + task[0][1] - task[0][0]
            time = time + task[0][1]
            sjobs.remove([task[0][0], task[0][1]])
        else:
            time = time + 1

    return tsum // len(jobs)