# http://www.spoj.com/problems/PRIME1/

crivo = [True] * 100000010
crivo[1] = False
crivo[0] = False

t = int(raw_input())

for i in xrange(t):
  a, b = map(int, raw_input().split())
  for j in xrange(a, b + 1):
    x = int(j)
    if crivo[j]:
      print j
  print

