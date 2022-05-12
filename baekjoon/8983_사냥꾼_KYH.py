import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    if y <= L:
        targets.append([x, y])

answer = 0
for x, y in targets:
    start, end = 0, M - 1
    while start < end:
        mid = (start + end) // 2
        if hunters[mid] < x:
            start = mid + 1
        else:
            end = mid
            
    if abs(hunters[end] - x) + y <= L or abs(hunters[end - 1] - x) + y < L:
        answer += 1
    
print(answer)