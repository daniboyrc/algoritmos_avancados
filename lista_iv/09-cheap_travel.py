n, m, a, b = map(int, raw_input().split())

money = 0
qtd = 0

if n >= m:
  if m * 1.0 / b > 1.0 / a:
    money = n // m * b
  else:
    money = n // m * m * a
  n = n % m
  

if b > n * a:
  money += n * a
else:
  money += b

print money
