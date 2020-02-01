cls = {}
def count():
    return int(input())

def read(string):
    if len(string) == 1:
        cls[string] = []
    else:
        child = string.replace(' ', '').split(':')[0]
        parent = string.split(':')[1].split()
        cls[child] = parent

for i in range(count()):
    string = str(input())
    read(string)

for i in range(count()):
    parent, child = str(input()).split()
    if parent in cls.get(child):
        print('Yes')
    else:
        print('No')



