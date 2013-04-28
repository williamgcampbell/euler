#!/usr/bin/env python

"""
To test the program:
    % python core_tests.py -v
"""

import unittest
import utils.core as core

class TestCore (unittest.TestCase) :
    def test_prime_gen(self) :
        g = core.prime_gen()
        self.assertEqual(g.next(), 2)
        
        for i in range(1, 100):
            g.next()
        
        self.assertEqual(g.next(), 547)	

if __name__ == '__main__':
    unittest.main()	