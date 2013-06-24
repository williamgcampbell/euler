from utils.numbers import factorial

def fds(n):
    '''
    Finds the sum of the digits of the factorial of n
    '''
    s = 0
    for c in str(factorial(n)):
        s += int(c)
    return s

print fds(100)