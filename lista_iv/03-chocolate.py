# http://codeforces.com/problemset/problem/617/B

def corta_extremos(lista):
    while lista[0] != 1:
        lista.pop(0)
    while lista[-1] != 1:
        lista.pop(-1)

num = raw_input()
lista = map(int, raw_input().split())

if 1 not in lista:
    print 0
else:
    corta_extremos(lista)
    soma = 0
    resultado = 1

    for i in range(1, len(lista)):
        if lista[i] == 0:
            soma += 1
        else:
            resultado *= soma + 1
            soma = 0
    print resultado
