# http://codeforces.com/problemset/problem/514/A

num = raw_input()
string = ""
if num[0] != "9" and num[0] > '4':
    string += str(9 - int(num[0]))
else:
    string += num[0]
for i in range(1, len(num)):
    if num[i] > '4':
        string += str(9 - int(num[i]))
    else:
        string += num[i]

print string
