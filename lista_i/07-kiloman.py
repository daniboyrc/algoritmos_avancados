num = int(raw_input())
for i in xrange(num):
  raw_input()
  tiros = map(int, raw_input().split())
  pulos = raw_input()
  atingido = 0
  for i in xrange(len(pulos)):
    if pulos[i] == 'J' and tiros[i] > 2:
      atingido += 1
    if pulos[i] == 'S' and tiros[i] <= 2:
      atingido += 1
  print atingido
    
