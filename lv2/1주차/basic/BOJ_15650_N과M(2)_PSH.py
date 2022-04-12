from collections import deque
import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
nums = list(range(1, n+1))
stack = deque()
answer = list()
for idx, i in enumerate(nums):
    stack.append([[str(i)], nums[idx+1:]])
while len(stack) > 0:
    temp, remain = stack.popleft()
    if len(temp) == m:
        answer.append(temp)
    if remain:
        for idx, i in enumerate(remain):
            new_temp = temp + [str(i)]
            stack.append([new_temp, remain[idx+1:]])

for x in answer:
    print(" ".join(x))
    
# 32452	KB 92 ms
