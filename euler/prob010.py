import timeit

n=2000000
def primes(n):
    '''
    Set of prime numbers < n
    '''
    assert n > 0
    assert type(n) == int
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

print timeit.Timer(stmt='primes.primes(2000000)', setup='import prob010 as primes').timeit(1)
print "The sum of all primes below two million is:", sum(primes(n))