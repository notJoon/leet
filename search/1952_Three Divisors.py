""" 
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m

>>> Input: n = 2
>>> Output: false

>>> Input: n = 4
>>> Output: true
"""
def isThree(n: int) -> bool:
    divisor = 1
    for i in range(1, n):
        if n % i == 0:
            divisor += 1 
                
        if divisor > 3:
            return False 
        
    ## n has exactly three positive divisors 
    return divisor == 3

### 

import unittest

class Test(unittest.TestCase):
    def test_example_1(self):
        self.assertFalse(isThree(2))
    
    def test_example_2(self):
        self.assertTrue(isThree(4))



if __name__ == '__main__':
    unittest.main()