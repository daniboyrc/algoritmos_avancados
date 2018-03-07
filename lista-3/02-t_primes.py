from math import sqrt
from sys import stdout

crivo = [True] * 1900000
crivo[1] = False
crivo[0] = False

for i in xrange(2, len(crivo)):
  if crivo[i]:
    for j in xrange(i*2, len(crivo), i):
      crivo[j] = False

raw_input()
lista = map(int, raw_input().split())

for i in lista:
  a = int(sqrt(i))
  if crivo[a] and a ** 2 == i : stdout.write('YES\n')
  else: stdout.write('NO\n')
