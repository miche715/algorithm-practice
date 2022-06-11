# https://programmers.co.kr/learn/courses/30/lessons/17680
# 캐시

def solution(size, cities):
    answer = 0
    cache = []
    
    for c in cities:
        city = c.upper()
        if city not in cache:
            cache.insert(0, city)
            if len(cache) > size:
                cache.pop()
            answer = answer + 5
        else:
            cache.pop(cache.index(city))
            cache.insert(0, city)
            answer = answer + 1
    
    return answer