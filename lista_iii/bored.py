num = map(int, raw_input().split())
num.sort()
num = num[0]

valor = 1
for i in xrange(2, num + 1):
    valor *= i

print valor
