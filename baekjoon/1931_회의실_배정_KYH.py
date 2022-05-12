import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1], x[0]))

answer = 0
temp = 0
for start, end in time:
    if start >= temp:
        answer += 1
        temp = end
print(answer)