from utils.core import is_prime
    
def lpf(n):
    '''
    Calculates the largest prime factor of a positive integer
    '''
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    if n == 1: return None
    return max(filter(
            is_prime,
            set(reduce(
                list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))