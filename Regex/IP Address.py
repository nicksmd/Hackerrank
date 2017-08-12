import re
n = int(raw_input())
for i in range(n):
    line = raw_input()
    if re.match(r'^((\d|[1-9]\d|1\d\d|2[0-5][0-5])\.){3}((\d|[1-9]\d|1\d\d|2[0-5][0-5]))$', line):
        print 'IPv4'
    else:
        if re.match(r'^((\d|[a-fA-F]){1,4}:){7}((\d|[a-fA-F]){1,4})$', line):
            print 'IPv6'
        else:
            print 'Neither'




