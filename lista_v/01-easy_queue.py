from collections import deque
from sys import stdin, stdout

fila = deque()

n = int(raw_input())
for i in xrange(n):
  entrada = stdin.readline().split()
  if entrada[0] == '1':
    fila.append(entrada[1])
  elif entrada[0] == '2':
    fila.popleft()
  else:
    try:
      stdout.write(fila[0]+'\n')
    except:
      stdout.write('Empty!\n')
