colunas = int(raw_input())
lista = raw_input().split()
lista = [int(a) for a in lista]

matriz = []
for i in range(colunas):
	matriz.append([])
	for j in range(max(lista)):
		if lista[i] <= i: 
			matriz[i].append([0])

for i in range(colunas):
	for j in range(max(lista)):
		if lista[i] >= i:
			print 1

print matriz
