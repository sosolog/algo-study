import math

def solution(s):
    length = len(s)
    mid = (length - 1) / 2
    answer = s[math.floor(mid) : math.ceil(mid)+1]
    return answer