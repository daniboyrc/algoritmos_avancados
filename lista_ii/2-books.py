num, temp = map(int, raw_input().split())
livros = map(int, raw_input().split())

soma, cont = 0, 0
x = 0
for i in range(num):
	soma += livros[i]
	cont += 1
	if soma > temp:
		cont -= 1
		soma -= livros[x]
		x += 1

print cont