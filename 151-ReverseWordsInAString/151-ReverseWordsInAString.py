class Solution:
    def reverseWords(self, s: str) -> str:

        """
        damn this actually kind of cooked me.

        i forgot that split existed, and i thought reverse returned something so for a few submissions i tried doing words = s.split().reverse()

        0 ms runtime beats 100
        """
        
        words = s.split()
        words.reverse()
        return " ".join(words)
        

        
