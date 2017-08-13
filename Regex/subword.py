import re
n = int(raw_input())
string =""
for i in range(n):
    string += (" "+raw_input())

m = int(raw_input())
for i in range(m):
    s = raw_input()
    if re.match(r"\w+", s):
        pattern = re.compile("\W?"+s+"\W")
        print len(re.findall(pattern, string))