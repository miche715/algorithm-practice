# https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일명 정렬

def solution(files):
    answer = []
    arr = []
    
    for f in files:
        tmp = ["", "", ""]
        flag = False
        for i in range(len(f)):
            if f[i].isdigit() and len(tmp[1]) < 5:
                flag = True
                tmp[1] = tmp[1] + f[i]
            else:
                if flag:
                    tmp[2] = f[i:]
                    break
                else:
                    tmp[0] = tmp[0] + f[i]
        arr.append(tmp)
    
    arr = sorted(arr, key = lambda x: (x[0].lower(), int(x[1])))
    
    for a in arr:
        answer.append("".join(a))
    
    return answer