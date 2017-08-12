import re
n = int(raw_input())
for i in range(n):
    line = raw_input()
    start = re.match(r'^hackerrank.*$', line)
    end = re.match(r'^.*hackerrank$', line)
    if start and end:
        print 0
    else:
        if start:
            print 1
        else:
            if end:
                print 2
            else:
                print -1



