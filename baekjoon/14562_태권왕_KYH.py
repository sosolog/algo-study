import sys
from collections import deque
input = sys.stdin.readline

def solution(S, T):
    C = 0
    q = deque()
    q.append([S, T, C])

    while q:
        S, T, C = q.popleft()
        if S < T:
            q.append([S * 2, T + 3, C+1])  # A
            q.append([S +1, T, C + 1])  # B
        elif S == T:
            return C

for _ in range(int(input())):
    S, T = map(int, input().split())
    print(solution(S, T))