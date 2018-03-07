while True:
	var = int(raw_input())
	if var == 0: break
	centro = raw_input().split()
	for i in range(var):
		cida = raw_input().split()
		pos = ''
		if cida[0] == centro[0] or cida[1] == centro[1]:
			pos = 'divisa'
		else:
			if int(cida[1]) > int(centro[1]):
				pos = 'N'
			if int(cida[1]) < int(centro[1]):
				pos = 'S'
			if int(cida[0]) < int(centro[0]):
				pos += 'O'
			if int(cida[0]) > int(centro[0]):
				pos += 'E'
		
		print pos

