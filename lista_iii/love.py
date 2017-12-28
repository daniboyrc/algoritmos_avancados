num = int(raw_input())
divisores = 1

for i in xrange(2, int(num) + 1):
    if num == 1:
        break
    while True:
        if num % i == 0:
            num /= i
            if divisores % i != 0:
                divisores *= i
        else:
            break
print divisores
