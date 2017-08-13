# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
for i in range(n):
    string = raw_input()
    if re.match(r"\([+-]?(([0-9]|[1-8][0-9])(\.\d+)?|90(.0+)?), [+-]?(([0-9]|[1-9][0-9]|1[0-7][0-9])(\.\d+)?|180(.0+)?)\)", string):
        print "Valid"
    else:
        print "Invalid"