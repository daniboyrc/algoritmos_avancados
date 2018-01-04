# http://codeforces.com/problemset/problem/520/A

num = int(raw_input())
palavra = raw_input()
d = []

for i in palavra:
    if i.lower() not in d:
        d.append(i.lower())

if len(d) == 26:
    print 'YES'
else:
    print 'NO'
 


