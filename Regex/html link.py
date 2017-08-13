import re
import sys

n = int(raw_input())
string = ""
for i in range(n):
    string += (' '+raw_input())

a_tag_pattern = re.compile(r"<a\s.*?/a>")

for a_tag in a_tag_pattern.findall(string):

    # re.match matches the pattern from the start of the string.
    # re.findall however searches for occurrences of the pattern anywhere in the string.

    link_pattern = re.compile(r"<a\s*href\s*=\s*[\"\'](.*?)[\"\']")
    link = link_pattern.match(a_tag).groups()
    sys.stdout.write(link[0].strip()+",")

    text_pattern = re.compile(r">([^<>]*?)<\s*\/")
    text = text_pattern.findall(a_tag)
    sys.stdout.write(text[0].strip() + "\n")



