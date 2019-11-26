
glob = {}

def parse(string):
    string = string.split(' ')


    if string[0] == 'add':
        namespace = string[1]
        var = string[2]
        if namespace not in glob:
            glob[namespace] = {}
            glob[namespace]['var'] = [var]



    if string[0] == 'create':
        namespace = string[1]
        parent = string[2]
        glob[parent][namespace] = {}

    if string[0] == 'get':
        namespace = string[1]
        var = string[2]




if __name__ == '__main__':
     n = int(input())
     while n > 0:
         string = str(input())
         parse(string)
         print(glob)
