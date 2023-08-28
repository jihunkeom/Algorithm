import heapq

def dijkstra(graph, start):
	distances = {node: float("inf") for node in graph}
	distances[start] = 0
	queue = []
	heapq.heappush(queue, [distances[start], start])

	while queue:
		current_distance, current_node = heapq.heappop(queue)

		if distances[current_node] < current_distance:
			continue

		for adjacent, weight in graph[current_node].items():
			distance = current_distance + weight
			if distance < distances[adjacent]:
				distances[adjacent] = distance
				heapq.heappush(queue, [distance, adjacent])
		
	return distances

V, E = map(int, input().split())
start = int(input())
graph = {}
for _ in range(E):
    u, v, w = map(int, input().split())
    if u in graph:
        if v not in graph[u]:
            graph[u].update({v:w})
        else:
            graph[u][v] = min(graph[u][v], w)
    else:
        graph[u] = {v:w}

for i in range(1, V+1):
    if i not in graph:
        graph[i] = {}
        
dist = dijkstra(graph, start)
for i in range(1, V+1):
    val = dist[i]
    if val == float("inf"):
        print("INF")
    else:
        print(val)