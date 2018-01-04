def find(v):
  if v == grafo[v]: return v
  return find(grafo[v])

def union(u,v):
  grafo[find(u)] = find(v)

grafo = dict()

# entrada
num_vert = int(raw_input())
for i in range(num_vert):
  x, y = map(int, raw_input().split())
  grafo[(x,y)] = (x,y)

for i in grafo:
  for j in grafo:
    if i != j:
      if i[0] == j[0] or i[1] == j[1]:
        if find(i) != find(j):
          union(i, j)
  
lista = []
for i in grafo:
  if find(i) not in lista:
    lista.append(find(i))
    
print len(lista) - 1
