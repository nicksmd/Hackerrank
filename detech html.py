import re
import sys
from collections import OrderedDict
n = int(raw_input())
input_list = []
for i in range(n):
    input_list.append(raw_input())

string = "\n".join(input_list)

dic = OrderedDict()

for tag, attr in sorted(re.findall(r"<(\w+)(\s+[^>]*|)>", string)):
    dic.setdefault(tag,[]).append(attr)

attr_set = set()
for tag, attrs in dic.items():
    sys.stdout.write(tag+":")
    for attr in attrs:
        attr_name_list = re.findall(r"(\w+)=[\"\'].*?[\"\']", attr)
        for attr_name in attr_name_list:
            attr_set.add(attr_name)

    print ",".join(sorted(attr_set))
    attr_set.clear()


