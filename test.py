import itertools

def primes():
    n = 1
    while True:
        n += 1
        if n % 2 == 0 and n != 2:
            continue
        for i in range(3, 10):
            x = True
            if i == n:
                x = False
                continue
            elif n % i == 0:
                x = False
                break
        if x == True:
            yield n


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
