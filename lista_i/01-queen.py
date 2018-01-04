while True:
	x1, y1, x2, y2 = raw_input().split()
	
	if x1 == '0': break
	elif x1 == x2 and y1 == y2: print '0'
	elif x1 == x2 or y1 == y2 or (abs(int(x2) - int(x1)) == abs(int(y2) - int(y1))): print '1'
	else: print '2'
