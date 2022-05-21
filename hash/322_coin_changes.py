""" Coin Changes 
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

>>> Input: coins = [1,2,5], amount = 11
>>> Output: 3

>>> Input: coins = [2], amount = 3
>>> Output: -1

>>> Input: coins = [1], amount = 0
>>> Output: 0
"""
from typing import Any, List 

def coinChange(coins: List[int], amount: int) -> int:
    pocket = {}
    def check_coin(amount: int):
        if amount in pocket:
            return pocket[amount]       
        if amount == 0:
            return 0    
        if amount < 0:
            return float("inf")
        
        pocket[amount] = min([1 + check_coin(amount - coin) for coin in coins])
        
        return pocket[amount]
    
    minimum = check_coin(amount)
    return minimum if minimum < float("inf") else -1

import unittest 

class Test(unittest.TestCase):

    coins: List[int]
    amount: int 
    input: Any
    expect: int 

    def test_example_1(self):
        coins = [1, 2, 5]
        amount = 11 
        input = coinChange(coins, amount)
        expect = 3
        self.assertEqual(input, expect)
    
    def test_example_2(self):
        coins = [2]
        amount = 3
        input = coinChange(coins, amount)
        expect = -1
        self.assertEqual(input, expect)
    
    def test_example_3(self):
        coins = [1]
        amount = 0 
        input = coinChange(coins, amount)
        expect = 0
        self.assertEqual(input, expect)


def coinChecking_using_dp(coins: List[int], amount: int) -> int:
    dp = [0] + [float("inf") for i in range(amount)]

    for i in range(1, amount+1):
        for coin in coins:
            if (i - coin) >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    if dp[-1] == float("inf"):
        return -1 
    
    return dp[-1]
    

if __name__ == "__main__":
    unittest.main()