crivo = [True] * 1000010
crivo[1] = False
crivo[0] = False

for i in xrange(2, len(crivo)):
  if crivo[i]:
    for j in xrange(i*2, len(crivo), i):
      crivo[j] = False

num = int(raw_input())

for i in xrange(num):
  a, b = map(int, raw_input().split())
  
  cont = 0
  for j in xrange(a, b + 1):
    if crivo[j]:
      if crivo[abs(j-2)] or crivo[abs(j+2)]:
        cont += 1
  
  print cont
