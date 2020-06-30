import itertools
def primes():
    n = 1
    while True:
        if n > 2:
            n += 2
        else:
            n += 1
        simple = True
        for i in range(3, n, 2):
            if n % i == 0:
                simple = False
                break
        if simple:
            yield n

print(list(itertools.takewhile(lambda x : x <= 31, primes())))