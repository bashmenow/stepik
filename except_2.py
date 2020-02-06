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

def check(klass, klass_list ):
    parents = cls.get(klass)
    if not parents:
        return False
    for i in parents:
        if i in klass_list:
            return True
        else:
            if check(i, klass_list):
                return True

for i in range(count()):
    string = str(input())
    read(string)

lst = []
for i in range(count()):
    string = str(input())
    lst.append(string)

lst = list(lst.__reversed__())
newlist = []
for i in lst:

    if check(i, lst[lst.index(i):]):
        newlist.append(i)

for i in range(len(newlist)):
    print(newlist.pop())



