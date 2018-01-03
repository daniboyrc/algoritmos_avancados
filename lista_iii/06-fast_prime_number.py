#https://www.urionlinejudge.com.br/judge/en/problems/view/1221

vezes = int(raw_input())
for i in xrange(vezes):
    num = int(raw_input())
    boole = False
    for i in xrange(2, int(num ** 0.5 + 2)):
        if num % i == 0:
            boole = True
            break

    if num == 2:
        print "Prime"
    elif boole or num == 1:
        print "Not Prime"
    else:
        print "Prime"

