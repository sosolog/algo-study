# 32380 KB 96 ms

from collections import deque

def dfs(graph, start, node_num):
	stack = deque()
	visited = [False]*node_num
	count = 0

	now = start
	while True:
		if not visited[now-1]:
			visited[now-1] = True
			count += 1

			if graph.get(now) is not None:
				for n in sorted(graph.get(now), reverse=True):
					if not visited[n-1]:
						stack.append(n)
		
		if len(stack) == 0:
			break
		
		now = stack.pop()

	return count -1

# main

node = int(input())
network = int(input())

graph = {}
for i in range(network):
	x, y = map(int, input().split())
	if graph.get(x) is None: graph[x] = [y]
	else: graph.get(x).append(y)
	if graph.get(y) is None: graph[y] = [x]
	else: graph.get(y).append(x)

print(dfs(graph, 1, node))
