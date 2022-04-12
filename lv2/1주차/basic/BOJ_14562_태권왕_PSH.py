from collections import deque
import sys


def dfs(a, b):
    stack = deque()
    stack.append((a, b, 0))

    candid = list()
    while len(stack) > 0:
        a, b, count = stack.popleft()
        if a == b:
            candid.append(count)
        elif a < b:
            stack.append((a * 2, b + 3, count + 1))
            stack.append((a + 1, b, count + 1))
    return str(min(candid))


c = int(sys.stdin.readline().rstrip())
answer = list()
for _ in range(c):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer.append(dfs(a, b))

print("\n".join(answer))

#32416 KB	344 ms
