import os
lst = []
for path, dirs, files in os.walk('main'):
    for file in files:
        if '.py' in file:
            lst.append(path)
            break
with open('stepik.txt', 'w') as txt:
    for i in sorted(lst):
        txt.write(i)
        txt.write('\n')

