# https://school.programmers.co.kr/learn/courses/30/lessons/250135
# 아날로그 시계

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start = (h1 * 3600) + (m1 * 60) + s1
    end = (h2 * 3600) + (m2 * 60) + s2

    h_operation = ""
    m_operation = ""
    for t in range(start, end + 1):
        if s1 >= 60:
            s1 = 0
            m1 = m1 + 1
            s_degree = 360
        else:
            s_degree = 0
        if m1 >= 60:
            m1 = 0
            h1 = h1 + 1
            m_degree = 360
        else:
            m_degree = 0
        if h1 >= 12:
            h = 0
            h_degree = 360
        else:
            h_degree = 0 
        h_degree = h_degree + ((h1 * 3600) + (m1 * 60) + (s1)) * (360 / 12 / 60 / 60)
        m_degree = m_degree + ((m1 * 60) + (s1)) * (360 / 60 / 60)
        s_degree = s_degree + s1 * (360 / 60)
        
        if t == start:  # 맨 처음 시작.
            if h_degree > s_degree:
                h_operation = "+"
            elif h_degree < s_degree:
                h_operation = "-"
            elif h_degree == s_degree:
                h_operation = "-"
                answer = answer + 1
                
            if m_degree > s_degree:
                m_operation = "+"
            elif m_degree < s_degree:
                m_operation = "-"    
            elif m_degree == s_degree:
                if h_degree != m_degree:
                    answer = answer + 1
                m_operation = "-"
        else:
            if h_degree <= s_degree and h_operation == "+":
                answer = answer + 1
                h_operation = "-"
            if h_degree > s_degree:
                h_operation = "+"
            
            if m_degree <= s_degree and m_operation == "+":
                if h_degree != m_degree:
                    answer = answer + 1
                m_operation = "-"
            if m_degree > s_degree:
                m_operation = "+"
                
        s1 = s1 + 1
        
    return answer

print(solution(0, 5, 30, 0, 7, 0))


"""
각도...
분침/초침, 시침/초침의 각도가 0도가 됐을 때 알람이 울려야 함.
시간은 연속적인 구조니까 그냥 1초 단위로 잘라서 1초전 각도가 -였는데 지금 각도가+가 됐다면 알람이 울림.

초침: 6도(360 / 60)
분침: 0.1도(360 / 60 / 60)
시침: 0.00833333333333333333333333333333도(360 / 12 / 60 / 60)

# 벡터 1: (x1, y1), 벡터 2: (x2, y2)
x1, y1 = 1, 1
x2, y2 = -1, 1
# 각도 계산
angle1 = math.atan2(y1, x1)
angle2 = math.atan2(y2, x2)
# 벡터 간의 각도 차이 (라디안)
angle_difference = angle1 - angle2
print(math.degrees(angle_difference))
"""