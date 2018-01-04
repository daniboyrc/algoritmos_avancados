n, m = map(int, raw_input().split())
for i in range(n):
	tipo = raw_input()
	cont = 0
	var = ""
	for k in tipo:
		if i % 2 == 0 and tipo[cont] == '.':
			if cont % 2 == 0:
				var += 'B'
			else:
				var += 'W'
		elif i % 2 == 1	and tipo[cont] == '.':
			if cont % 2 == 0:
				var += 'W'
			else:
				var += 'B'
		else:
			var += '-'
		cont += 1
	print var
