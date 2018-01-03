def soma(num):
  if int(num) < 10: return num
  s = 0
  for i in num:
    s += int(i)
  return soma(str(s))
  

while True:
  a, b = raw_input().split()
  if a == '0' and b == '0':
    break
  if soma(a) > soma(b): print 1
  elif soma(a) < soma(b): print 2
  else: print 0
