import re
n = int(raw_input())
count = 0
for i in range(n):
    line = raw_input()
    if re.match(r'.*hackerrank.*', line, re.IGNORECASE):
        count+=1

print count




