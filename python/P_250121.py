# https://school.programmers.co.kr/learn/courses/30/lessons/250121
# 데이터 분석

def solution(data, ext, val_ext, sort_by):
    index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    return sorted(filter(lambda x: x[index[ext]] < val_ext, data), key=lambda x: x[index[sort_by]])