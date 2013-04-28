from utils.core import prime_gen

gen = prime_gen()
for i in range(1, 10001):
    next(gen)

print "The 10001st prime number is:", next(gen)