import sys
input = sys.stdin.readline
answer = 0
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
visited = [False] * (n + 1)
def dfs(v):
    global answer
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            answer += 1
    
dfs(1)
print(answer)