def isPrime(n):
    # make sure n is a positive integer
    assert n > 0
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def primeFactor(n):
    gpf=1
    factors = (lambda x: list(sum(((i, x//i) for i in range(1, int(x**0.5) + 1) if x % i == 0), ())))(n)
    for factor in factors:
        if isPrime(factor) and factor > gpf:
            gpf = factor
    return gpf
    
print "The largest prime factor of the number 600851475143 is:", primeFactor(600851475143)