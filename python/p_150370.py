# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 개인정보 수집 유효기간

def solution(today, terms, privacies):
    termDictionary = {}
    answer = []
    
    for t in terms:
        term, period = t.split(" ")
        termDictionary[term] = int(period) * 28
    
    year, month, day = today.split(".")
    today = ((int(year) - 2000) * 12 * 28) + (int(month) * 28) + int(day)
    
    for i in range(len(privacies)):
        date, term = privacies[i].split(" ")
        year, month, day = date.split(".")
        if((((int(year) - 2000) * 12 * 28) + (int(month) * 28) + int(day) - 1) + termDictionary[term] < today):
            answer.append(i + 1)
        
    return answer