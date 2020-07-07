import sys
import re
pattern = r'((\w)\2+)'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r'\2', line))