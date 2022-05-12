import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]

min_line = 1
max_line = max(line)

while min_line <= max_line:
    mid = (min_line + max_line) // 2
    cnt = 0
    for l in line:
        cnt += l // mid
    if cnt >= N:
        min_line = mid + 1
    else:
        max_line = mid - 1

print(max_line)