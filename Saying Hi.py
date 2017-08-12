import re
n = int(raw_input())
for i in range(n):
    line = raw_input()
    if re.match(r'^[Hh][Ii]\s[^Dd].*$', line):
        print line