""" 
Given two strings s and t, 
return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

>>> Input: s = "ab#c", t = "ad#c"
>>> Output: true

>>> Input: s = "ab##", t = "c#d#"
>>> Output: true 

>>> Input: s = "a#c", t = "b"
>>> Output: false
"""

import string


def backspaceCompare(s: str, t: str) -> bool:
    def compare(_string):
        save = []
        for s in _string:
            if s != '#':
                    save.append(s)
            else:
                    save = save[:-1]
        return save
        
    return compare(s) == compare(t)

###

import unittest

class Test(unittest.TestCase):
    def test_backspace_once(self):
        s = "ab#c" 
        t = "ad#c"
        self.assertTrue(backspaceCompare(s, t))
    
    def test_backspacce_twice(self):
        s = "ab##"
        t = "c#d#"
        self.assertTrue(backspaceCompare(s, t))
    
    def test_backspace_but_not_equal(self):
        s = "a#c"
        t = "b"
        self.assertFalse(backspaceCompare(s, t))

if __name__ == "__main__":
    unittest.main()
