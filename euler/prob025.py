from utils.sequence import fibonacci_gen

def fibn(n):
    '''
    Finds the first term of the Fibonacci sequence containing n digits
    return a tuple (index, number) that first matches 
    '''
    i = 0
    g = fibonacci_gen()
    for f in g:
        i+=1
        if len(str(f)) == n:
            return (i, f)

print fibn(1000)