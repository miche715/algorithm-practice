# https://school.programmers.co.kr/learn/courses/30/lessons/250135
# 아날로그 시계

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = (h1 * 3600) + (m1 * 60) + s1
    end = (h2 * 3600) + (m2 * 60) + s2
    prev_h_degree = -1
    prev_m_degree = -1
    prev_s_degree = -1
    
    for t in range(start, end + 1):
        if s1 >= 60:
            s1 = s1 - 60
            m1 = m1 + 1
        if m1 >= 60:
            m1 = m1 - 60
            h1 = h1 + 1
        if h1 >= 12: 
            h1 = h1 - 12
        h_degree = ((h1 * 3600) + (m1 * 60) + s1) * (360 / 12 / 60 / 60)
        m_degree = ((m1 * 60) + s1) * (360 / 60 / 60)
        s_degree = s1 * (360 / 60)
        if t == start:
            if h_degree == s_degree:
                answer = answer + 1
            if m_degree == s_degree:
                answer = answer + 1
            if h_degree == m_degree == s_degree:
                answer = answer - 1
        else:
            if h_degree <= s_degree and prev_h_degree > prev_s_degree:
                answer = answer + 1
            elif s_degree == 0 and prev_h_degree > prev_s_degree:
                answer = answer + 1
            if m_degree <= s_degree and prev_m_degree > prev_s_degree:
                answer = answer + 1
            elif s_degree == 0 and prev_m_degree > prev_m_degree:
                answer = answer + 1
            if h_degree % 360 == m_degree % 360 == s_degree % 360:
                answer = answer - 1
        prev_h_degree = h_degree
        prev_m_degree = m_degree
        prev_s_degree = s_degree
        s1 = s1 + 1

    return answer