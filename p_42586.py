# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

def solution(progresses, speeds):
    answer = []
    date = []

    for i in range(len(progresses)):
        quo = (100 - progresses[i]) // speeds[i]
        rem = (100 - progresses[i]) % speeds[i]

        if rem > 0:
            quo = quo + 1

        date.append(quo)

    cnt = 1
    for i in range(len(date) - 1):
        if date[i] >= date[i + 1]:
            cnt = cnt + 1
            date[i + 1] = date[i]
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer