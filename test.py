def first(x):
    return x.isdigit()


def second(x):
    return x.isalpha()


lst = ['1', '6', 'd', 'gh', 'rf', '6', 'f', 'vd', '45', 'yg', '3', '6', '0', 'fr']

print([i for i in filter(second, lst)])