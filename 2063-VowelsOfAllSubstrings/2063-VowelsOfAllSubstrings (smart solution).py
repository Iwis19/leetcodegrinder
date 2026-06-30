class Solution:
    

    def countVowels(self, word: str) -> int:

        """
        from solutions. im dum today.

        51 ms runtime beats 80%
        """
        
        n = len(word)
        res = 0
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            
            if word[i] in VOWELS:
                res += (i + 1) * (n - i)
                
        return res
                
