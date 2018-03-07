while True:
	var = int(raw_input())
	if var == 0: break
	
	vez = raw_input()	
	vez = [int(n) for n in vez.split()]

	if len(vez) == 1: print '0'
	else:
		picos = 0
		for i in range(1, len(vez) - 1):
			if vez[i] > vez[i+1] and vez[i] > vez[i-1]:
				picos += 1
			elif vez[i] < vez[i+1] and vez[i] < vez[i-1]:
				picos += 1
		
		if vez[0] > vez[1] and vez[0] > vez[-1]:
			picos += 1
		elif vez[0] < vez[1] and vez[0] < vez[-1]:
			picos += 1
		
		if vez[-1] > vez[0] and vez[-1] > vez[-2]:
			picos += 1
		if vez[-1] < vez[0] and vez[-1] < vez[-2]:
			picos += 1
		
		print picos

