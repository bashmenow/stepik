import sys
import re
pattern = r'\b(\w)(\w)(\w*)\b'
for line in sys.stdin:
    line = line.rstrip()
    obj = re.findall(pattern, line)
    print(obj)
    print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line))