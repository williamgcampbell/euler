#Multiples of 3 and 5 below 1000
print eval join '+', grep { !($_ % 3 and $_ % 5) } 1 .. 999;
#answer: 233168