# 32472 KB	352 ms

from collections import deque

def dfs(g, s_node, n_num):
	s = deque()
	order = []
	isVisited = {}

	now = s_node

	while True:
		# print(isVisited)
		if isVisited.get(now) is None:
			isVisited[now] = True
			order.append(str(now))

			if g.get(now) is not None :
				for n_idx in sorted(g.get(now), reverse=True):
					if isVisited.get(n_idx) is None:
						s.append(n_idx)
		if len(s) == 0 or len(isVisited) == n_num: 
			break
		
		now = s.pop()
		
	return " ".join(order)

def bfs(g, s_node, n_num):
	que = deque()
	order = []
	isVisited = {}

	now = s_node
	while True:
		# print(isVisited)
		if isVisited.get(now) is None:
			isVisited[now] = True
			order.append(str(now))

			if g.get(now) is not None :
				for n_idx in sorted(g.get(now)):
					if isVisited.get(n_idx) is None:
						que.append(n_idx)

		if len(que) == 0 or len(isVisited) == n_num: 
			break
		
		now = que.popleft()
		
	return " ".join(order)

# 메인

n, m, v = map(int, input().split())
graph = {}

for i in range(0, m):
	x, y = map(int, input().split())
	if graph.get(x) is None: graph[x] = [y]
	else: graph[x].append(y)
	if graph.get(y) is None: graph[y] = [x]
	else: graph[y].append(x)

# print(graph)
print(dfs(graph, v, n))
print(bfs(graph, v, n))
