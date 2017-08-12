import re
n = int(raw_input())
for i in range(n):
    line = raw_input()
    if re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', line):
        print 'YES'
    else:
        print 'NO'




