caso = 1
while True:
  n, q = map(int, raw_input().split())
  if n == 0 or q == 0: break
  
  mbr = [0] * 100010
  pos = [-1] * 100010
  
  for i in range(n):
    mbr[int(raw_input())] += 1
    
  if (mbr[0] > 0):
    pos[0] = 0
  for i in range(1, 100001):
    if (mbr[i] > 0):
      pos[i] = mbr[i-1]
    mbr[i] += mbr[i-1]
  
  print 'CASE# %i:' % caso
  for i in range(q):
    a = int(raw_input())
    if (pos[a] == -1):
      print a, 'not found'
    else:
      print '%i found at %i' %(a, pos[a] + 1)

  caso += 1
