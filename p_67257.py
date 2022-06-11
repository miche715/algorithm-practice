# https://programmers.co.kr/learn/courses/30/lessons/67257
# 수식 최대화

import re
import copy

def solution(expression):
    answers = []
    rank = [['*','+','-'], ['*','-','+'], ['-','*','+'], ['-','+','*'], ['+','-','*'], ['+','*','-']]
    numbersa = re.split("[+ | * | -]", expression)
    symbolsa = re.findall("[+ | * | -]", expression)
    
    for i in rank:
        numbers = copy.deepcopy(numbersa)
        symbols = copy.deepcopy(symbolsa)
        for j in i:
            while j in symbols:
                ex = ''
                number = symbols.index(j)
                ex = numbers.pop(number) + symbols.pop(number) + numbers.pop(number)
                numbers.insert(number,str(eval(ex)))
        answers.append(abs(int(numbers[0])))

    return max(answers)