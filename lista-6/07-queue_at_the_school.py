num, temp = map(int, raw_input().split())
fila = raw_input()
array = []

for i in fila:
	array.append(i)

for i in range(temp):
	new_fila = ""
	trocou = False
	for i in range(len(array) - 1):
		if trocou:
			trocou = False
		else:
			if array[i] == "B" and array[i+1] == "G":
				array[i+1] = "B"
				array[i] = "G"
				trocou = True

print "".join(array)
