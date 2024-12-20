# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 둘만의 암호

def solution(encryption, skip, index):
    decryption = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for s in skip:
        alphabet.remove(s)
        
    for e in encryption:
        decryption = decryption + alphabet[(alphabet.index(e) + index) % len(alphabet)]
    
    return decryption