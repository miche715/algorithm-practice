# https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 바탕화면 정리

def solution(wallpaper):
    miny, minx, maxy, maxx = 51, 51, -1, -1
    
    for i in range(len(wallpaper)):
        file = list(wallpaper[i])
        for j in range(len(file)):
            if file[j] == "#":
                if i <= miny:
                    miny = i
                if i >= maxy:
                    maxy = i
                if j <= minx:
                    minx = j
                if j >= maxx:
                    maxx = j
    
    return [miny, minx, maxy + 1, maxx + 1]