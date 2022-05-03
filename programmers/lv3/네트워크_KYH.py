def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def DFS(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] and not visited:
                DFS(j)

    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer