""" 1410. HTML Entity Parser
HTML entity parser is the parser that takes HTML code as input and replace all the entities 
of the special characters by the characters itself.

The special characters and their entities for HTML are:

    Quotation Mark: the entity is &quot; and symbol character is ".
    Single Quote Mark: the entity is &apos; and symbol character is '.
    Ampersand: the entity is &amp; and symbol character is &.
    Greater Than Sign: the entity is &gt; and symbol character is >.
    Less Than Sign: the entity is &lt; and symbol character is <.
    Slash: the entity is &frasl; and symbol character is /.

Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.
"""
import unittest
import re

class Solution:
    def __init__(self) -> None:
        self.tokens = {
            '&quot;' : '"',
            '&apos;' : "'",
            '&amp;' : '&',
            '&gt;' : '>',
            '&lt;' : '<',
            '&frasl;' : '/'
        }
        
    def entityParser(self, text: str) -> str:
        regex = re.compile(r"&[a-zA-Z]+;", re.S)
        return regex.sub(self.pattern_match, text)
    
    def pattern_match(self, pattern: dict):
        if pattern.group(0) in self.tokens:
            return self.tokens.get(pattern.group(0))
        else:
            return pattern.group(0)