from itertools import permutations

# 소수판별
def checkPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    per = []
    new_per = []
    set_per = []
    
    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))
    
    for p in per:
        new_per.append(int(("").join(p)))
        
    # 중복제거
    for n in new_per:
        if n not in set_per:
            set_per.append(n)
    
    for s in set_per:
        if checkPrime(s):
            answer += 1   
    return answer