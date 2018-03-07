# http://codeforces.com/problemset/problem/617/A

num = int(raw_input())
resultado = num // 5
if num % 5 != 0:
    resultado += 1
print resultado
