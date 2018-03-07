# https://www.urionlinejudge.com.br/judge/en/problems/view/2584

import math

vezes = int(raw_input())
for i in xrange(vezes):
    num = float(raw_input())
    num = num ** 2 * math.tan(math.radians(54)) * 5 / 4
    
    print "%.3f" % num

