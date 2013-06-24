_cache = {1: 1, 2: 2, 3: 8, 6: 9, 7: 17, 9: 20, 18: 21, 25: 24, 27: 112, 54: 113, 73: 116, 97: 119,
          129: 122, 171: 125, 231: 128, 313: 131, 327: 144, 649: 145, 703: 171, 871: 179, 1161: 182,
          2223: 183, 2463: 209, 2919: 217, 3711: 238, 6171: 262, 10971: 268, 13255: 276, 17647: 279,
          23529: 282, 26623: 308, 34239: 311, 35655: 324, 52527: 340, 77031: 351, 106239: 354,
          142587: 375, 156159: 383, 216367: 386, 230631: 443, 410011: 449, 511935: 470, 837799: 525,
          1117065: 528, 2234130: 529, 2978841: 532, 3971787: 535, 4707303: 543, 5573991: 551,
          5649499: 613, 7532665: 616}
_DEFAULT_MAX_CACHE_SIZE=200000
_DEFAULT_MAX_KEY_SIZE=10000000
def collatz_length(n, max_cache_size=_DEFAULT_MAX_CACHE_SIZE, max_key_size=_DEFAULT_MAX_KEY_SIZE):
    '''
    Return the collatz length of n.
    '''
    if n == 1:
        return 1
    
    if n in _cache:
        return _cache[n]
    
    if n == ((n >> 1) << 1):
        l = collatz_length((n >> 1)) + 1
    else:
        l = collatz_length((n + (n >> 1) + 1)) + 2
        
    if len(_cache) < max_cache_size and l < max_key_size:
        _cache[n] = l
    return l
 
def longest_collatz(n, m):
    '''
    Returns a tuple of the (number, chain length) of the longest collatz path between n and m
    '''
    ml, l = (0, 0)
    for x in xrange(m, n-1, -1):
        l = collatz_length(x)
        if l > ml:
            t = (x, l)
            ml = l
    return t

print longest_collatz(1, 1000000)