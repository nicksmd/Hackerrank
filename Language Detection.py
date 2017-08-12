import re
import sys

src = ''.join(sys.stdin.readlines())

if 'java' in src:
    print("Java")
elif '#include' in src:
    print("C")
else:
    print("Python")