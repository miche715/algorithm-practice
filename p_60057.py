# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축

def solution(s):
    answer = len(s)
    tmpstr = ""

    for i in range(1, int(len(s) / 2) + 1):
        cnt = 1

        for j in range(0, len(s), i):
            block = s[j : j + i]

            if s[j : j + i] == s[j + i : j + i + i]:
                cnt = cnt + 1
            else:
                if cnt > 1:
                    tmpstr = tmpstr + str(cnt) + block
                else:
                    tmpstr = tmpstr + block

                cnt = 1

        if len(tmpstr) < answer:
            answer = len(tmpstr)

        tmpstr = ""

    return answer