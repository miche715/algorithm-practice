# https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 광물 캐기

def solution(picks, minerals):
    answer = 0
    stemina_diamond_pick = {"diamond": 1, "iron": 1, "stone": 1}
    stemina_iron_pick = {"diamond": 5, "iron": 1, "stone": 1}
    stemina_stone_pick = {"diamond": 25, "iron": 5, "stone": 1}
    stemina_ranking = {}
    
    if (picks[0] + picks[1] + picks[2]) * 5 < len(minerals):
         minerals = minerals[:(picks[0] + picks[1] + picks[2]) * 5]

    stemina_sum = 0
    stemina_key = []
    for i, mineral in enumerate(minerals):
        stemina_sum = stemina_sum + stemina_stone_pick[mineral]
        stemina_key.append(i)
        if i % 5 == 4:
            stemina_ranking[tuple(stemina_key)] = stemina_sum
            stemina_sum = 0
            stemina_key.clear()
    if stemina_sum > 0:
        stemina_ranking[tuple(stemina_key)] = stemina_sum
    
    for sr in sorted(stemina_ranking.items(), key=lambda x: x[1], reverse=True):
        for i in sr[0]:
            if picks[0] > 0:
                pick = 0
                answer = answer + stemina_diamond_pick[minerals[i]]
            elif picks[1] > 0:
                pick = 1
                answer = answer + stemina_iron_pick[minerals[i]]
            elif picks[2] > 0:
                pick = 2
                answer = answer + stemina_stone_pick[minerals[i]]
        picks[pick] = picks[pick] - 1

    return answer