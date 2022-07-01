""" Zig Zag Conversation
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

>>> Input: s = "PAYPALISHIRING", numRows = 3
>>> Output: "PAHNAPLSIIGYIR"

>>> Input: s = "PAYPALISHIRING", numRows = 4
>>> Output: "PINALSIGYAHRPI"
"""
import unittest

def convert(string: str, rows: int) -> str:
    if rows == 1:
        return string 
    
    lines = [''] * rows
    curr, zig = 0, 1
    
    for c in string:
        lines[curr] += c
        
        if curr == 0:
            zig = 1
        
        elif curr == rows - 1:
            zig = -1
        
        curr += zig
    
    return ''.join(lines)

class Test(unittest.TestCase):

    string: str 
    rows: int 
    expect: str 

    def test_example_1(self):
        string = "PAYPALISHIRING"
        rows = 3
        expect = "PAHNAPLSIIGYIR"
        self.assertEqual(convert(string, rows), expect)

    def test_example_2(self):
        string = "PAYPALISHIRING"
        rows = 4
        expect = "PINALSIGYAHRPI"
        self.assertEqual(convert(string, rows), expect) 

if __name__ == '__main__':
    unittest.main()