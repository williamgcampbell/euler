def primes(n):
    '''
    Set of prime numbers less than n
    '''
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
        
def is_prime(n):
    '''
    Determines the primality of n
    '''
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    
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

def gpf(n):
    '''
    Calculates the greatest prime factor of a positive integer
    '''
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    if n == 1: return None
    return max(filter(
            is_prime,
            set(reduce(
                list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))

def factorial(n):
    '''
    Finds the factorial of n
    '''
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num