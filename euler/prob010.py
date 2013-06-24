import timeit
from utils.numbers import primes

n=2000000
print timeit.Timer(stmt='primes(2000000)', setup='from __main__ import primes').timeit(1)
print "The sum of all primes below two million is:", sum(primes(n))