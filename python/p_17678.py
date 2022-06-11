# https://programmers.co.kr/learn/courses/30/lessons/17678
# 셔틀버스

def makeHHMM(time):
    hhmm = str(time // 60) + ":" + str(time % 60)
    if hhmm[1] == ":":
        hhmm = "0" + hhmm
    if len(hhmm) == 4:
        t = list(hhmm)
        t.insert(3, "0")
        hhmm = "".join(t)
    
    return hhmm

def solution(n, t, m, timetable):
    wait = []
    hh = 9 * 60
    cnt = 1  # 셔틀이 지금 몇번 왔다갔다 했는지
    
    for tt in timetable:
        wait.append(int(tt[:tt.index(":")]) * 60 + int(tt[tt.index(":") + 1:]))
    wait.sort()
    
    while cnt < n:
        take = 0  # 셔틀에 탑승한 크루의 수
        for w in wait:
            if w <= hh:
                take = take + 1
            if take == m or w > hh:
                for _ in range(take):
                    if wait:
                        wait.pop(0)
                    else:
                        break
                break
        hh = hh + t
        cnt = cnt + 1
        
    #  반복문을 빠져 나왔을 때 hh가 마지막 셔틀이 오는 시간
    #  즉 셔틀을 타고 싶으면 아무리 늦어도 hh까지는 와야함
    #  근데 남아있는 크루가 있을 수 있음
    #  크루가 셔틀을 기다리러 온 시간과 hh를 따져서 answer를 정해야 함
    take = 0
    for w in wait:
        if w > hh:
            return makeHHMM(hh)
        else:
            take = take + 1 
        if take == m:
            return makeHHMM(w - 1)
    return makeHHMM(hh)