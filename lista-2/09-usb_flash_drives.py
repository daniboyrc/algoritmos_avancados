num_pendrives = int(raw_input())
armazenamento = int(raw_input())

sizes = []
for i in range(num_pendrives):
    j = int(raw_input())
    sizes.append(j)

sizes.sort()
sizes.reverse()
soma, cont = 0, 0

for i in sizes:
    if soma >= armazenamento:
        break
    soma += i
    cont += 1

print cont
	