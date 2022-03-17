import sys
from collections import deque
input = sys.stdin.readline

n, m, k, start = map(int, input().split())
visited = [False] * (n + 1)
distance = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    distance[a].append(b)
 
answer = []
q = deque([start])
visited[start] = True
distance[start] = 0

while q:
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            distance[i] = distance[now] + 1
            if distance[i] == k:
                answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)