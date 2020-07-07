import sys
import re
pattern = r'\b[a,A]+\b'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'argh', line, 1))
