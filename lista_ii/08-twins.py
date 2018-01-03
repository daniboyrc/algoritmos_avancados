num = int(raw_input())
lista = map(int, raw_input().split())

metade = sum(lista) / 2
lista.sort()
lista.reverse()
soma, cont = 0, 0
for i in lista:
	soma += i
	cont += 1
	if soma > metade:
		break

print cont