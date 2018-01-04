def find(v):
  if v == parents[v]: return v
  return find(parents[v])

def union(u,v):
  parents[find(u)] = find(v)

def parents(e):
  lista = []
  for i in range(e):
    lista.append(i)
  return lista

labels = []
zeros = 0
# entrada
num_e, num_l = map(int, raw_input().split())
parents = parents(num_e)
for i in range(num_e):
  e = map(int, raw_input().split())
  if e[0] == 0: zeros += 1
  labels.append(e[1:])

lista = []
for i in range(len(labels)):
  for j in range(len(labels)):
    if find(i) != find(j):
      for k in labels[i]:
        for l in labels[j]:
          if k == l:
            union(i, j)

for i in parents:
  if find(i) not in lista:
    lista.append(find(i))

b = True
for i in labels:
  if i != []:
    b = False

if b:
  print zeros
else:
  print len(lista) - 1
