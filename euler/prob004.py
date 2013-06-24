import timeit
from utils.strings import is_palindrome

def largest_product_palindrome(low, high):
    '''
    Calculates the largest palindrome made from the product of two numbers starting with low and ending with high
    '''
    return max(filter(is_palindrome, [str(x*y) for x in range(low, high) for y in range(x, high)]) + [None])
    
def largest_product_palindrome_e(low, high):
    '''
    A faster implementation of calculating the largest palindrome  made from the product of two numbers between high and low
    '''
    l = None
    for x in range(low, high):
        for y in range(x, high):
            p = x*y
            if is_palindrome(str(p)): l = max(p, l)
    return l
    
print "Faster:", largest_product_palindrome_e(1000, 2000)
print timeit.Timer(stmt='largest_product_palindrome_e(100, 1000)', setup='from __main__ import largest_product_palindrome_e').timeit(10)    
    
print "Shorthand:", largest_product_palindrome(1000, 2000)
print timeit.Timer(stmt='largest_product_palindrome(100, 1000)', setup='from __main__ import largest_product_palindrome').timeit(10)