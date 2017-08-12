import re
pattern = re.compile('^(\d{1,3})[ -](\d{1,3})[ -](\d{4,10})$')
n = int(raw_input())
for i in range(n):
    line = raw_input()
    group = pattern.match(line).groups()
    if group:
        print 'CountryCode=%s,LocalAreaCode=%s,Number=%s' % group
