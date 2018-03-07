n = int(raw_input())
for i in xrange(n):
  lista = []
  
  for j in xrange(5):
    lista.append(map(int, raw_input().split()))
  
  print lista[0][0]
  for j in xrange(1, 5):
    for k in xrange(j):
      x = abs(lista[j][k] + lista[j][k+1] - lista[j-1][k]) / 2
      print lista[j][k] + x, lista[j][k+1] + x,
    print
    for k in xrange(j):
      x = abs(lista[j][k] + lista[j][k+1] - lista[j-1][k]) / 2
      print lista[j][k], x,
    print lista[j][-1]
    
    
