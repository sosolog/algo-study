import math

def solution(n):
    n_sqrt = math.sqrt(n)
    total = 0
    for i in range(1, math.ceil(n_sqrt)):
        if(n % i == 0):
            total += (i + n / i)
    if n_sqrt == int(n_sqrt): 
        total += n_sqrt
    return total