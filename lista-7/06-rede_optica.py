def find(x):
    if graph[x] == x:
        return x
    return find(graph[x])
 
def union(u, v):
    graph[find(u)] = find(v)
 
cont = 0
while True:
    cont += 1
    edges = []
    v, e = map(int, raw_input().split())
 
    if v == 0:
        break
	
    graph = dict()
    for i in xrange(v):
        graph[i + 1] = i + 1
 
    for i in xrange(e):
        u, v, c = map(int, raw_input().split())
        edges.append((c, u, v))
 
    edges.sort()
 
    arvore = []
    for c, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            arvore.append([u, v])
 
    print "Teste ", cont
    for i in arvore:
        i.sort()
        print i[0], i[1]
    print 
