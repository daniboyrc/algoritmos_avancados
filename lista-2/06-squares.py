#http://codeforces.com/problemset/problem/263/B

n, k = map(int, raw_input().split())
lista = map(int, raw_input().split())
lista.sort()
lista.reverse()

if k > n:
  print -1
else:
  print lista[k - 1], lista[k - 1]
