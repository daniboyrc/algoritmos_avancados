num = int(raw_input())
lista = map(int, raw_input().split())

sereja = 0
dima = 0
vez = 1

for i in range(num):
	valor = 0
	if lista[0] >= lista[-1]:
		valor = lista.pop(0)
	else:
		valor = lista.pop()

	if vez:
		sereja += valor
		vez = 0
	else:
		dima += valor
		vez = 1

print sereja, dima