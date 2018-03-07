#http://codeforces.com/problemset/problem/546/B

raw_input()
lista = map(int, raw_input().split())
lista.sort()

cont = 0
for i in xrange(1, len(lista)):
  while lista[i] <= lista[i - 1]:
    lista[i] += 1
    cont += 1
print cont


