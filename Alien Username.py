import re
n = int(raw_input())
for i in range(n):
    line = raw_input()
    if re.match(r'^[_\.][0-9]+[a-zA-Z]*_*$', line):
        print 'VALID'
    else:
        print 'INVALID'



