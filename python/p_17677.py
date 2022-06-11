# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링

def solution(str1, str2):
    strstr1 = []
    strstr2 = []
    intersection = []  # 교집합
    union = []  # 합집합

    for i in range(len(str1) - 1):
        c1 = str1[i].upper()
        c2 = str1[i + 1].upper()
        if ord(c1) < 65 or ord(c1) > 90:
            continue
        if ord(c2) < 65 or ord(c2) > 90:
            continue
        strstr1.append(c1 + c2)

    for i in range(len(str2) - 1):
        c1 = str2[i].upper()
        c2 = str2[i + 1].upper()
        if ord(c1) < 65 or ord(c1) > 90:
            continue
        if ord(c2) < 65 or ord(c2) > 90:
            continue
        strstr2.append(c1 + c2)

    temp = strstr2.copy()
    for i in strstr1:
        if i in temp:
            intersection.append(i)
            temp.remove(i)

    union = strstr1 + strstr2
    temp = intersection.copy()
    for i in union:
        if i in temp:
            union.remove(i)
            temp.remove(i)

    if len(strstr1) == 0 and len(strstr2) == 0:
        answer = 1 * 65536
    else:
        answer = int((len(intersection) / len(union)) * 65536)

    return answer