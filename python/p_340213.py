# https://school.programmers.co.kr/learn/courses/30/lessons/340213?
# 동영상 재생기

def solution(video_len, pos, op_start, op_end, commands):
    total_length = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    current_pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    openning_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    openning_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    
    for command in commands:
        if openning_start <= current_pos <= openning_end:
            current_pos = openning_end
        
        if command == "next":
            current_pos = current_pos + 10
        elif command == "prev":
            current_pos = current_pos - 10
        
        if current_pos >= total_length:
            current_pos = total_length
        elif current_pos <= 0:
            current_pos = 0
        
        if openning_start <= current_pos <= openning_end:
            current_pos = openning_end
    
    return str(current_pos // 60).zfill(2) + ":" + str(current_pos % 60).zfill(2)