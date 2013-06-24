def power_digit_sum(n, p):
    '''
    Returns the sum of the digits of the n to the power of p
    '''
    return sum(map(int,str(n**p)))
    
if __name__ == "__main__":
    import time
    print "Power digit sum problem:"
    n = raw_input("Number: ")
    n = int(n)
    p = raw_input("Power: ")
    p = int(p)
    start = time.strftime('%s')
    s = power_digit_sum(n, p)
    end = time.strftime('%s')
    time = int(end) - int(start)
    print "Sum of the digits =", s
    print "Time to execute the algorithm =", time ,"Second(s)"
