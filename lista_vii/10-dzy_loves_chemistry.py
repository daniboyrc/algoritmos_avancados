def find(v):
  if v == grafo[v]: return v
  return find(grafo[v])

def union(u,v):
  grafo[find(u)] = find(v)

def grafo(n):
  lista = []
  for i in range(n + 1):
    lista.append(i)
  return lista

n, m = map(int, raw_input().split())
grafo = grafo(n)
lista = []
for i in range(m):
  lista.append(map(int, raw_input().split()))

soma = 0
for i in lista:
  if find(i[0]) != find(i[1]):
    soma += 1
    union(i[0], i[1])
    
print 2**soma
