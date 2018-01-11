while True:
  p, s = map(int, raw_input().split())
  if p == 0: break
  
  traps = map(int, raw_input().split())
  n = int(raw_input())
  
  players = [0] * p
  booleans = [False] * p
  
  pos = 0
  for i in xrange(n):
    
    if pos >= len(booleans): pos = 0
    
    while booleans[pos]:
      booleans[pos] = False
      pos += 1
      if pos >= len(booleans): pos = 0
      
    casas = sum(map(int, raw_input().split()))
    
    players[pos] += casas
    
    if players[pos] in traps:
      booleans[pos] = True
    
    if players[pos] >= s + 1:
      print pos + 1
      break
    
    pos += 1
      
