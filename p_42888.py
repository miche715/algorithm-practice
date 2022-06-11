# https://programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방

def solution(record):
    answer = []
    temp = []
    user = {}

    for i in range(len(record)):
        cmd = record[i].split(" ")

        if cmd[0] == "Enter":
            user[cmd[1]] = cmd[2]
            temp.append(cmd[1] +"@님이 들어왔습니다.")
        elif cmd[0] == "Leave":
            temp.append(cmd[1] +"@님이 나갔습니다.")
        elif cmd[0] == "Change":
            user[cmd[1]] = cmd[2]

    for i in range(len(temp)):
        temp[i] = temp[i].split("@")
        temp[i][0] = user[temp[i][0]]
        answer.append(temp[i][0] + temp[i][1])

    return answer