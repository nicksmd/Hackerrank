import re
n = int(raw_input())
string = ""
for i in range(n):
    string = string + ' '+ raw_input()

m = int(raw_input())

for i in range(m):
    word = raw_input()
    groups = re.match("(.*)(our)(.*)",word).groups()
    prefix = groups[0]
    suffix = groups[2]

    words = re.sub('our', 'o[u]?r', word)
    print words

    regex = re.compile("\\b"+words+"\\b", re.IGNORECASE)
    words = regex.finditer(string)
    print(len(list(words)))

