# https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 광물 캐기

def solution(picks, minerals):
    answer = 0
    stemina_dict = {"diamond": 2, "iron": 1, "stone": 0}
    stemina_rate = {}
    
    stemina_sum = 0
    stemina_key = []
    for i, mineral in enumerate(minerals):
        stemina_sum = stemina_sum + stemina_dict[mineral]
        stemina_key.append(i)
        if i % 5 == 4:
            stemina_rate[tuple(stemina_key)] = stemina_sum
            stemina_sum = 0
            stemina_key.clear()
    if stemina_sum > 0:
        stemina_rate[tuple(stemina_key)] = stemina_sum
    
    
    # 아직 푸는 중...      
    

    return answer

solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])