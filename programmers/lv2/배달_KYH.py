import sys

def solution(N, road, K):
    answer = 0

    start = 1
    graph = [[] for _ in range(N+1)]  # 주어진 그래프 정보
    visited = [False] * (N+1)  # 방문 처리 기록
    distance = [sys.maxsize] * (N+1)  # 거리 테이블
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    # 시작노드
    visited[start] = 0
    distance[start] = 0

    # 시작노드의 인접 노드에 대해 최단거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작노드 제외 다른 노드들 처리
    for _ in range(N-1):
        # 방문X 시작노드와 최단거리의 노드
        now = 0
        min_distance = sys.maxsize
        for i in range(1, N+1):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                now = i
        visited[now] = True

        # 위 노드와 인접한 노들들 간의 거리 계산
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
    
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    return(answer)

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))