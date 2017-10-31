def restos(x):
    return x % 3


lista = map(int, raw_input().split())
lista.sort()
restos = map(restos, lista)
restos.sort()
flores = 0
bl = True
for i in lista:
    flores += i / 3
if restos == [0, 2, 2]:
    flores += 1
print flores
