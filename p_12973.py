# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기

def solution(s):
    strli = list(s)
    strst = []

    while True:
        if len(strli) == 0:
            break
        if len(strli) >= 2:
            if strli[len(strli) - 1] == strli[len(strli) - 2]:
                strli.pop()
                strli.pop()
            else:
                if len(strst) > 0:
                    if strli[len(strli) - 1] == strst[len(strst) - 1]:
                        strli.pop()
                        strst.pop()
                    else:
                        strst.append(strli.pop())
                else:
                    strst.append(strli.pop())
        else:
            if len(strst) > 0:
                if strli[len(strli) - 1] == strst[len(strst) - 1]:
                    strli.pop()
                    strst.pop()
                else:
                    strst.append(strli.pop())
            else:
                break

    if len(strli) == 0 and len(strst) == 0:
        answer = 1
    else:
        answer = 0

    return answer