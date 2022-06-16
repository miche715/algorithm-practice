def solution(n):
    answer = 0
    stack = []
    
    while n >= 3:
        stack.append(str(n % 3))
        n = n // 3
    stack.append(str(n))
        
    answer = int("".join(stack), 3)
    
    return answer

print(solution(78413450))