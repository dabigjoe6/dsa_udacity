import math

class GraphNode:
	def __init__(self, value):
		self.value = value
		self.edges = []

	def addEdge(self, node, weight):
		self.edges.append(GraphEdge(node, weight))

	def removeEdge(self, node):
		self.edges.remove(node)

class GraphEdge:
	def __init__(self, node, weight):
		self.node = node
		self.weight = weight

class Graph:
	def __init__(self, nodes):
		self.nodes = nodes

	def addEdge(self, node1, node2, weight):
		if node1 in self.nodes and node2 in self.nodes:
			node1.addEdge(node2, weight)
			node2.addEdge(node1, weight)

	def removeEdge(self, node1, node2):
		if node1 in self.nodes and node2 in self.nodes:
			node1.removeEdge(node2)
			node2.removeEdge(node1)

	def getShortestDistanceNode(self, distanceObject):
		shortest_distance = float('inf')
		shortest_distance_node = None

		for node in distanceObject:
			if distanceObject[node] < shortest_distance:
				shortest_distance = distanceObject[node]
				shortest_distance_node = node
		return shortest_distance_node

	def dijkstra(self, start_node):
		if not start_node in self.nodes:
			return None

		shortest_distance = {}
		visited = {}
		unvisited = {}

		for each_node in self.nodes:
			shortest_distance[each_node] = float("inf")
			unvisited[each_node] = float("inf")
		
		shortest_distance[start_node] = 0
		unvisited[start_node] = 0

		current_node = self.getShortestDistanceNode(unvisited)

		while len(visited) != len(self.nodes):
			# print(len(visited))
			# print(len(self.nodes))
			for edge in current_node.edges:
				if (shortest_distance[current_node] + edge.weight) < shortest_distance[edge.node]:
					shortest_distance[edge.node] = shortest_distance[current_node] + edge.weight
					unvisited[edge.node] = shortest_distance[current_node] + edge.weight

			visited[current_node] = None
			del unvisited[current_node]
			current_node = self.getShortestDistanceNode(unvisited)

		for node in shortest_distance:
			print("Shortest distance to node " + str(node.value) + " from " + str(start_node.value) + " is: " + str(shortest_distance[node]))


node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.addEdge(node_u, node_a, 4)
graph.addEdge(node_u, node_c, 6)
graph.addEdge(node_u, node_d, 3)
graph.addEdge(node_d, node_u, 3)
graph.addEdge(node_d, node_c, 4)
graph.addEdge(node_a, node_u, 4)
graph.addEdge(node_a, node_i, 7)
graph.addEdge(node_c, node_d, 4)
graph.addEdge(node_c, node_u, 6)
graph.addEdge(node_c, node_i, 4)
graph.addEdge(node_c, node_t, 5)
graph.addEdge(node_i, node_a, 7)
graph.addEdge(node_i, node_c, 4)
graph.addEdge(node_i, node_y, 4)
graph.addEdge(node_t, node_c, 5)
graph.addEdge(node_t, node_y, 5)
graph.addEdge(node_y, node_i, 4)
graph.addEdge(node_y, node_t, 5)

print(graph.dijkstra(node_u))