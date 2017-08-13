import re

n = int(raw_input())
string = ""
for i in range(n):
    string += (' '+raw_input())

result = set()

pattern = re.compile(r"\w[\w\.]*@\w+.[\w.]+\w")

for tag in pattern.findall(string):
    result.add(tag.strip())

print ";".join(sorted(result))






