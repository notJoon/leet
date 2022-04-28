"""#771. Jewels and Stones
    You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.  
    Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    >>> Input: jewels = "aA", stones = "aAAbbbb"
    >>> Output: 3
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0 
        
        # count stones
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        # sum every jewels
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        
        return count 