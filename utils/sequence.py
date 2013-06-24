def prime_gen() :
    '''
    A prime number generator
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

def fibonacci_gen() :
    '''
    A fibonacci number generator
    '''
    a, b = 0, 1
    while True:
        a, b = a + b, a
        yield a
