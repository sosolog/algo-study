from collections import deque

def solution(n, edge):
    answer = 0
    q = deque()
    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q.append(1)
    distance[1] = 1

    while q:
        now = q.popleft()
        for g in graph[now]:
            if distance[g] == 0:
                q.append(g)
                distance[g] = distance[now]+1

    answer = distance.count(max(distance))
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))