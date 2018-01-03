#https://www.urionlinejudge.com.br/judge/en/problems/view/2232

vezes = int(raw_input())

for i in xrange(vezes):
    num = int(raw_input())
    soma = 0
    for i in xrange(1, num):
        soma += 2 ** i
    print soma + 1
