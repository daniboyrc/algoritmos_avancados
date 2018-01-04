b = int(raw_input())
list_b = map(int, raw_input().split())
list_b.sort()
g = int(raw_input())
list_g = map(int, raw_input().split())
list_g.sort()

cont = 0
p1 = 0
p2 = 0

menor = list_b
maior = list_g

while p1 <= len(menor) - 1 and p2 <= len(maior) - 1:
	if abs(menor[p1] - maior[p2]) <= 1:	
		cont += 1
		p1 += 1
		p2 += 1
	elif menor[p1] < maior[p2]:
		p1 += 1
	elif menor[p1] > maior[p2]:
		p2 += 1

print cont

