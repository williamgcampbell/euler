def isPrime(n):
    assert n > 0
    if n < 2: return False
    if n == 2: return True    
    if not n & 1: return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True
    
def lpf(n):
    assert type(n) == int and n > 0, "n must be a positive integer"
    gpf=1
    factors = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
    for factor in factors:
        if isPrime(factor) and factor > gpf:
            gpf = factor
    return gpf