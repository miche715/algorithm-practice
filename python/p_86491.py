# https://programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형

def solution(sizes):
    xsize = []
    ysize = []
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        xsize.append(sizes[i][0])
        ysize.append(sizes[i][1])
    xsize.sort(reverse = True)
    ysize.sort(reverse = True)
    
    return xsize[0] * ysize[0]