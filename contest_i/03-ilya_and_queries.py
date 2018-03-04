from sys import stdin, stdout

pos = raw_input()

array = [0] * (len(pos) + 2)

cont = 0
for i in xrange(1, len(pos)):
	if pos[i-1] == pos[i]:
		cont += 1
	array[i] = cont
	

num = int(raw_input())
for i in xrange(num):
	a, b = map(int, raw_input().split())
	stdout.write(str(abs(array[a-1] - array[b-1])) + '\n')
