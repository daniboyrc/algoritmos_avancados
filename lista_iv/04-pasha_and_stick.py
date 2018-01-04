# http://codeforces.com/problemset/problem/610/A

num = int(raw_input())
if num <= 4:
    print 0
elif num % 4 == 0:
    print num / 4 - 1
elif num % 4 == 2:
    print num // 4
else:
    print 0

