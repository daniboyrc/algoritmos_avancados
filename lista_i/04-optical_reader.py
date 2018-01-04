letras = ['A', 'B', 'C', 'D', 'E']

while True:
	n = int(raw_input())
	if n == 0: break
	for i in range(n):
		alt = raw_input().split()
		
		marcadas = []
		for j in range(len(alt)):
			if int(alt[j]) <= 127:
				marcadas.append(j)
		if len(marcadas) > 1 or len(marcadas) == 0:
			print '*'
		else:
			print letras[marcadas[0]]

