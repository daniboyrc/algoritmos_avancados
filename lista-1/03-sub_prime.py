while True:
  b, n = map(int, raw_input().split())
  if n == 0: break
  
  banks = map(int, raw_input().split())

  for i in xrange(n):
    x, y, z = map(int, raw_input().split())
    banks[x-1] -= z
    banks[y-1] += z
  
  b = True
  for i in banks:
    if i < 0:
      b = False
      break
  
  if b: print 'S'
  else: print 'N'
