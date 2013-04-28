n = r = 0
while not r:
    n += 20
    #is the length of the list of elements divisible by n (excluding 1) equal to high - low
    r = (lambda x: len([i for i in xrange(2, 21) if x % i == 0]) == 19)(n)

print "The smallest positive number evenly divisible by all numbers from 1 to 20 is:", n