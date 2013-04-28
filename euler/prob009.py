def gcd(a, b):
    while b:
        a, b = b, a%b
    return a



print "There exists exactly one Pythagorean triplet for which a + b + c = 1000, the product of abc is:", r