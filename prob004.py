def isPalindrome(n):
    return str(n) == str(n)[::-1]
    
def largestProductPalindrome(first, last):
    largest = 0
    for x in range(last, first, -1):
        for y in range(last, first, -1):
            product = x*y
            if isPalindrome(product):
                largest = product if product > largest else largest
    return largest
    
print "The largest palindrome made from the product of two 3-digit numbers is:", largestProductPalindrome(100, 999)