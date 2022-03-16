# 119096 KB	4024 ms
# 성공 (다익스트라 + bfs)
# 현재 탐색 노드에서 연결된 노드 중 방문하지 않은 곳을 큐에 담고,
# 다음 탐색 노드를 큐에서 하나 빼는 형식.. 

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

candidates_map = dict()
for _ in range(M):
	p1, p2 = map(int, sys.stdin.readline().rstrip().split())
	if not p1 in candidates_map:
		candidates_map[p1] = list()
	candidates_map[p1].append(p2)

visited = [False for _ in range(N+1)]
price = [2**31-1 for _ in range(N+1)]
visited[0] = True
price[0] = -1

start = X
price[start] = 0

q = deque()
q.append(start)

while len(q) > 0:
	start = q.popleft()
	visited[start] = True
		
	candidates = candidates_map.get(start)
	if candidates:
		for candi in candidates:
			if not visited[candi]:
				temp_price = price[start] + 1
				price[candi] = min(price[candi], temp_price)
				q.append(candi)


answer = list()
for node in range(1, N+1):
	if price[node] == K:
		answer.append(node)

if len(answer) == 0:
	print(-1)
else :
	for a in answer:
		print(a)
