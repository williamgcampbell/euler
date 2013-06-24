def prime_gen() :
    '''
    Generates an infinite sequence of prime numbers
    '''
    # map composites to primes witnessing their compositeness
    D = {}
    
    # integer to test for primality
    q = 2
    
    while True:
        if q not in D:
            # yield, an unmarked composite must be a prime
            yield q
            
            # mark the first multiple of q
            D[q*q] = [q]
        else:
            # move each witness to its next multiple
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
                
            # D[q] has been reached and is no longer needed
            del D[q]
        q += 1
        
def is_prime(n):
    '''
    Determines the primality of n
    '''
    assert isinstance(n, int), "is_prime takes an int as it's argument"
    
    # 0 and 1 are not primes
    if n < 2: return False
    
    # 2 is the only even prime
    if n == 2: return True
    
    # all other even numbers are not prime
    if not n & 1: return False
    
    # range starting with 3 and going up to the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0: return False
    return True