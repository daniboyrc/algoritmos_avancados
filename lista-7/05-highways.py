from heapq import heappush, heappop

def dijkstra(s, c, num_vert, graph):
	visit = [False] * (num_vert + 1)
	dist = [9999999999] * (num_vert + 1)
	h = []
	heappush(h, ((0, s)))
	
	while h:
		v = heappop(h)
		if visit[v[1]] == True:
			continue
		visit[v[1]] = True
		
		dist[v[1]] = v[0]
		for e in graph[v[1]]:
			if v[0] + e[1] < dist[e[0]]:
				heappush(h, ((v[0] + e[1], e[0])))

	if dist[c] == 9999999999:
		return 'NONE'
	return dist[c]

def cria_grafo(v):
	grafo = []
	for i in xrange(v + 1):
		grafo.append([])
	return grafo

loop = int(raw_input())
for i in xrange(loop):
	v, k, saida, chegada = map(int, raw_input().split())
	grafo = cria_grafo(v)
	for j in range(k):
		a, b, c = map(int, raw_input().split())
		grafo[a].append((b, c))
		grafo[b].append((a, c))

	print dijkstra(saida, chegada, v, grafo)
