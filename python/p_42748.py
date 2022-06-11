# https://programmers.co.kr/learn/courses/30/lessons/42748
# K번째수

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        arr = array[commands[i][0]-1 : commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2] - 1])
        arr.clear()

    return answer