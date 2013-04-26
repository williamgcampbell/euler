def sumSquareDifference(n, m):
    sumOfSquares = sum((lambda x, y: [i**2 for i in xrange(x, y+1)])(n, m))
    squareOfSum = (lambda x, y: sum(xrange(x, y+1))**2)(n, m)
    return squareOfSum - sumOfSquares
    
print "The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: ", sumSquareDifference(1, 100)