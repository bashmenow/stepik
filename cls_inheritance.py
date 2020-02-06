cls = {}
def count():
    return int(input())

def read(string):
    if len(string.split()) == 1:
        cls[string] = []
    else:
        child = string.replace(' ', '').split(':')[0]
        parent = string.split(':')[1].split()
        cls[child] = parent

def check(parent, child):
    parents = cls.get(child)
    if not parents:
        return False
    for i in parents:
        if i == parent:
            return True
        else:
            if check(parent, i):
                return True

for i in range(count()):
    string = str(input())
    read(string)


for i in range(count()):
   parent, child = str(input()).split()
   if parent == child:
       print('Yes')
   elif check(parent, child):
       print('Yes')
   else:
       print('No')




