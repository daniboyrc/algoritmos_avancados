# http://codeforces.com/problemset/problem/584/A

n, t = raw_input().split()

if int(n) == 1 and t == "10":
    print -1
elif t == "10":
    print ("1" * (int(n) - 1)) + "0"
else:
	print t * int(n) 