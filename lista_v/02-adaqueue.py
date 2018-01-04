# http://www.spoj.com/problems/ADAQUEUE/

from collections import deque

num = int(raw_input())
d = deque()
reverse = False
for i in xrange(num):
    cm = raw_input().split()
    if cm[0] == "toFront":
        if reverse:
             d.append(cm[1])
        else:
             d.appendleft(cm[1])
    elif cm[0] == "push_back":
        if reverse:
            d.appendleft(cm[1])
        else:
            d.append(cm[1])
    if cm[0] == "reverse":
        reverse = not reverse
    elif len(d) == 0:
        print "No job for Ada?"
    elif cm[0] == "front":
        if reverse:
            print d.pop()
        else:
            print d.popleft()
    elif cm[0] == "back":
        if reverse:
            print d.popleft()
        else:
            print d.pop()
