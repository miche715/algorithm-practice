# https://school.programmers.co.kr/learn/courses/30/lessons/340198
# 공원

def check_mat(mat, park, start, end):
    for i in range(start, start + mat):
        for j in range(end, end + mat):
            if i < len(park) and j < len(park[0]):
                if park[i][j] != "-1":
                    return False
            else:
                return False
            
    return True
    
def solution(mats, park):
    answer = 0
    mats.sort(reverse = True)
    
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if check_mat(mat, park, i, j):
                    return mat
    
    return -1