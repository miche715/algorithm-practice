# https://programmers.co.kr/learn/courses/30/lessons/17683
# 방금그곡

def solution(m, musicinfos):
    answer = "(None)"
    sharp = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a",}
    length = 0
    
    for s in sharp.keys():
        if s in m:
            m = m.replace(s, sharp[s])
    
    for i in reversed(musicinfos):
        music = i.split(",")
        stime = music[0].split(":")
        etime = music[1].split(":")
        duration = (int(etime[0]) - int(stime[0])) * 60 + (int(etime[1]) - int(stime[1]))
        title = music[2]
        for s in sharp.keys():
            if s in music[3]:
                music[3] = music[3].replace(s, sharp[s])
        melody = music[3] * (duration // len(music[3])) + music[3][:duration % len(music[3])]
        if m in melody:
            if duration >= length:
                answer = title
                length = duration
    
    return answer