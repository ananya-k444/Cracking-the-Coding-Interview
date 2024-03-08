def dfs(graph, visited, node):
	if visited[node]:
		return

	visited[node] = True

	for neighbor in graph[node]:
		dfs(graph, visited, neighbor)


def isConnected(graph, source, dest):
	visited = [False] * len(graph)

	dfs(graph, visited, source)

	return visited[dest]


graph = {
	0: [1], 
	1: [2],
	2: [0, 3],
	3: [3]
}

print(isConnected(graph, 1, 3))
print(isConnected(graph, 3, 1))
