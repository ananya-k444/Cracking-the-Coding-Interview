from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# BFS 
	def isReachable(self, s, d):
		visited = [False] * self.V

		q = []
		q.append(s)
		visited[s] = True

		while q:
			node = q.pop(0)

			if node == d:
				return True

			for i in self.graph[node]:
				if visited[i] == False:
					q.append(i)
					visited[i] = True

		return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 3)

u = 1; v = 3
if g.isReachable(u, v):
	print("There is a path between nodes %d and %d" % (u, v))
else:
	print("There is NO path between nodes %d and %d" % (u, v))

u = 3; v = 1
if g.isReachable(u, v):
	print("There is a path between nodes %d and %d" % (u, v))
else:
	print("There is NO path between nodes %d and %d" % (u, v))
