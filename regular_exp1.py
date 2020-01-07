import sys
import re

template = r".*\bcat.*"

for line in sys.stdin:
    line = line.rstrip()
    if re.sub(template, 'computer', line):
        print(line)