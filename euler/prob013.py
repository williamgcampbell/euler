cache = {1:1}
def collatz_length(n):
    '''
    Return the collatz length of n.
    '''
    if not n in cache:
        cache[n] = collatz_length((n + (n >> 1) + 1) if n == ((n >> 1) << 1) else (n >> 1)) + 1
    return cache[n]
 
def longest_collatz(n, m):
    '''
    Returns a tuple of the (number, chain length) of the longest collatz path between n and m
    '''
    ml, l = (0, 0)
    for x in range(m-1, n-1, -1):
        l = _cache[x] if x in _cache.keys() else collatz_length(x)
        if l > ml:
            t = (x, l)
            ml = l
    return t

if __name__ == "__main__":
    import time
    limit = raw_input("Max limit: ")
    limit = int(limit)
    index = raw_input("Starting Number: ")
    index = int(index)
    start = time.strftime('%s')
    t = longest_collatz(index, limit)
    end = time.strftime('%s')
    time = int(end) - int(start)
    print "(Number, Chain Length) =", t
    print "Time to execute the algorithm =", time ,"Second(s)"






