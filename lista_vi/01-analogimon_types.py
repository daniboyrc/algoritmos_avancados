from sys import stdin, stdout

def dfs(graph, node, visited):
  if node not in visited:
    visited.append(node)
    for n in graph[node]:
        dfs(graph,n, visited)
  return visited

while True:
  try:
    n, m = map(int, stdin.readline().split())
    
    grafo = []
    for i in xrange(n + 1):
      grafo.append([])
    
    for i in xrange(m):
      a, b = map(int, stdin.readline().split())
      grafo[a].append(b)
      grafo[b].append(a)
    
    especie = int(raw_input())
    
    stdout.write(str(len(dfs(grafo, especie, []))) + '\n')
  except:
    pass
