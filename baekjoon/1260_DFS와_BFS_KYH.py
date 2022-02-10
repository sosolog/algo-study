from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited = [False] * (n + 1)
    q = deque([v])
    visited[v] = True
    while q:
        pop = q.popleft()
        print(pop, end=" ")
        for i in graph[pop]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
print()
bfs(v)
