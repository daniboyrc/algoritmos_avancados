num = int(raw_input())
lista = map(int, raw_input().split())
lista.sort()

bol = 'NO'
i = 0
li = len(lista)

while i != li - 2:
    if lista[i] == lista[i + 1]:
        lista.pop(i)
        i -= 1
        li = len(lista)
    elif lista[i] == lista[i + 2]:
        lista.pop(i)
        i -= 1
        li = len(lista)
    elif lista[i + 1] == lista[i + 2]:
        lista.pop(i + 1)
        i -= 1
        li = len(lista)
    elif abs(lista[i] - lista[i + 1]) > 2:
        pass
    elif abs(lista[i] - lista[i + 2]) > 2:
        pass
    elif abs(lista[i + 1] - lista[i + 2]) > 2:
        pass
    else:
        bol = 'YES'
    i += 1

print bol
