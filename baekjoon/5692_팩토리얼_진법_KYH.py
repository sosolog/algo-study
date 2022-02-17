import sys
import math
input = sys.stdin.readline

while True:
    num = input().strip()
    answer = 0
    if num == '0':
        break
    
    for i in range(len(num)):
        answer += int(num[i]) * math.factorial(len(num)-i)
    print(answer)