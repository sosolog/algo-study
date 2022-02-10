from collections import deque

def dfs(g, s_node):
	n_num = len(g)
	s = deque()
	order = []
	isVisited = {}

	now = s_node

	while True:
		if isVisited.get(now) is None:
			isVisited[now] = True
			order.append(str(now))
	
			for n_idx in range(n_num, 0, -1):
				if isVisited.get(n_idx) is None and g[now-1][n_idx-1] == 1:
					s.append(n_idx)

		if len(s) == 0 or len(isVisited) == n_num: 
			break
		
		now = s.pop()
		
	return " ".join(order)

def bfs(g, s_node):
	n_num = len(g)
	que = deque()
	order = []
	isVisited = {}

	now = s_node
	while True:
		if isVisited.get(now) is None:
			isVisited[now] = True
			order.append(str(now))
	
			for n_idx in range(1,n_num+1):
				if isVisited.get(n_idx) is None and g[now-1][n_idx-1] == 1:
					que.append(n_idx)

		if len(que) == 0 or len(isVisited) == n_num: 
			break
		
		now = que.popleft()
		
	return " ".join(order)


n, m, v = map(int, input().split())
graph = [[0]*n for _ in range(0,n)]

for i in range(0, m):
	x, y = map(int, input().split())
	graph[x-1][y-1] = 1
	graph[y-1][x-1] = 1

print(dfs(graph, v))
print(bfs(graph, v))
