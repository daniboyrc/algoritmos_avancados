#http://codeforces.com/problemset/problem/588/B
num = int(raw_input())
divisores = 1

for i in xrange(2, int(num ** 0.5) + 1):
    if num == 1:
        break
    while True:
        if num % i == 0:
            num /= i
            if divisores % i != 0:
                divisores *= i
        else:
            break
if num != 1:
	divisores *= num
print divisores

