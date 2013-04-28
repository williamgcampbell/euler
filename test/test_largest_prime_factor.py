#!/usr/bin/env python

"""
To test the program:
    % python largest_prime_factor.py -v
"""

import unittest
from euler.prob003 import lpf

class TestLPF (unittest.TestCase) :
    def test_largest_prime_factor(self) :
        self.assertEqual(lpf(600851475143), 6857)

    @unittest.expectedFailure
    def test_largest_prime_factor_failure(self):
        primeFactor(-4)

    @unittest.expectedFailure
    def test_largest_prime_factor_type_failure(self):
        primeFactor("12")
    
if __name__ == '__main__':
    unittest.main()	