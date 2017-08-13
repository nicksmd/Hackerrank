import re

n = int(raw_input())
string = ""
for i in range(n):
    string += (' '+raw_input())

result = set()

pattern = re.compile(r"https?:\/\/(www2?\.)?(([A-Za-z0-9-]+\.)+[A-Za-z0-9]+)")

for tag in pattern.findall(string):
    result.add(tag[1].strip())

print ";".join(sorted(result))






