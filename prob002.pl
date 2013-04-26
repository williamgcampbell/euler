#Sum of even-valued terms of the Fibonacci sequence whose values do not exceed four million
$x = 0;
print eval join '+', grep { $_ % 2 } map{ int($_ + 0.5) } map { $x = $_ == 0 ? 1/sqrt(5) : $x * (sqrt(5) + 1)/2 } 0 .. 33;
#answer: 4613732